from pymongo import MongoClient
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()


# Connect to MongoDB

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")

url = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"

mongo_client = MongoClient(url)

mongo_db = mongo_client["test_db092024"]
mongo_authors = mongo_db["authors"]
mongo_quotes = mongo_db["quotes"]

# Fetch messages
migrate_authors = list(mongo_authors.find())
migrate_quotes = list(mongo_quotes.find())


#  Connect to Postgres
conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
)
cur = conn.cursor()


# # Insert migrated authors
# for author in migrate_authors:
#     insert_query = """INSERT INTO quotes_author (fullname, born_date, born_location, description)
#     VALUES (%s, %s, %s, %s);"""
#     cur.execute(insert_query, (author["fullname"], author["born_date"], author["born_location"], author["description"]))
#     conn.commit()

#  # # Insert migrated quotes
# for quote in migrate_quotes:
#     for author in migrate_authors:
#         if author["_id"] == quote["author"]:
#             author_id = author["fullname"]
#             insert_query = """INSERT INTO quotes_quote (quote, author_id, tags)
#             VALUES (%s, (SELECT id FROM quotes_author WHERE fullname = %s), %s);"""
#             cur.execute(insert_query, (quote["quote"], author_id, quote["tags"]))
#     conn.commit()

def fill_tags():
    for quote in migrate_quotes:
        for tag in quote["tags"]:
            insert_query = """INSERT INTO quotes_tag (name) VALUES (%s)
            ON CONFLICT (name) DO NOTHING;"""
            cur.execute(insert_query, (tag, ))
        conn.commit()

def fill_quote_tag():
    for quote in migrate_quotes:
        for tag in quote["tags"]:
            insert_query = """INSERT INTO quotes_quote_tags (quote_id, tag_id)
                      VALUES ((SELECT id FROM quotes_quote WHERE quote = %s), 
                      (SELECT id FROM quotes_tag WHERE name = %s));"""
            cur.execute(insert_query, (quote["quote"], tag))
        conn.commit()

# fill_tags()
# fill_quote_tag()
# # Close connections
cur.close()
conn.close()
