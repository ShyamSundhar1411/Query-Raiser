# Generated by Django 4.1.1 on 2022-10-03 16:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("services", "0004_rename_query_raisedquery"),
    ]

    operations = [
        migrations.RenameModel(old_name="RaisedQuery", new_name="Query",),
    ]
