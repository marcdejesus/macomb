# Generated by Django 5.1.7 on 2025-03-13 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_add_missing_timestamp_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, null=True),
        ),
    ]
