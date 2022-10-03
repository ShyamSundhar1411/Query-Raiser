# Generated by Django 4.1.1 on 2022-10-03 14:06

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Query",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("date_of_creation", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending Approval", "Pending Approval"),
                            ("Approved", "Approved"),
                            ("Rejected", "Rejected"),
                        ],
                        max_length=200,
                    ),
                ),
                ("description", tinymce.models.HTMLField()),
                (
                    "department",
                    models.CharField(
                        choices=[
                            (
                                "Computer Science & Engineering(BCE)",
                                "Computer Science & Engineering(BCE)",
                            ),
                            (
                                "Science and Engineering with Specialisation in Artificial Intelligence and Machine Learning(BAI)",
                                "Science and Engineering with Specialisation in Artificial Intelligence and Machine Learning(BAI)",
                            ),
                            (
                                "Computer Science and Engineering with Specialisation in Cyber Physical Systems(BPS)",
                                "Computer Science and Engineering with Specialisation in Cyber Physical Systems(BPS)",
                            ),
                            (
                                "Computer Science and Engineering with Specialisation in Artificial Intelligence and Robotics(BRS)",
                                "Computer Science and Engineering with Specialisation in Artificial Intelligence and Robotics(BRS)",
                            ),
                            (
                                "M.Tech. Software Engineering(MIS)",
                                "M.Tech. Software Engineering(MIS)",
                            ),
                            (
                                "Computer Science and Engineering with Specialisation in Business Analytics(MIA)",
                                "Computer Science and Engineering with Specialisation in Business Analytics(MIA)",
                            ),
                        ],
                        max_length=200,
                    ),
                ),
                ("type", models.CharField(max_length=100)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        blank=True, editable=True, populate_from="title", unique=True
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "contact",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, region=None
                    ),
                ),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False, populate_from="user.username", unique=True
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]