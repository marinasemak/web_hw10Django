# Generated by Django 5.1.2 on 2024-11-04 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0002_tag_remove_quote_tags_quotetag"),
    ]

    operations = [
        migrations.RenameField(
            model_name="quotetag",
            old_name="quote_id",
            new_name="quote",
        ),
        migrations.RenameField(
            model_name="quotetag",
            old_name="tag_id",
            new_name="tag",
        ),
    ]