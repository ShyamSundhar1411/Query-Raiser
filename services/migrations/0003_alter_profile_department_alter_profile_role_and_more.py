# Generated by Django 4.1.1 on 2022-10-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0002_alter_profile_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="department",
            field=models.CharField(
                choices=[
                    (
                        "Computer Science & Engineering - BCE",
                        "Computer Science & Engineering - BCE",
                    ),
                    (
                        "Science and Engineering with Specialisation in Artificial Intelligence and Machine Learning - BAI",
                        "Science and Engineering with Specialisation in Artificial Intelligence and Machine Learning - BAI",
                    ),
                    (
                        "Computer Science and Engineering with Specialisation in Cyber Physical Systems - BPS",
                        "Computer Science and Engineering with Specialisation in Cyber Physical Systems - BPS",
                    ),
                    (
                        "Computer Science and Engineering with Specialisation in Artificial Intelligence and Robotics - BRS",
                        "Computer Science and Engineering with Specialisation in Artificial Intelligence and Robotics - BRS",
                    ),
                    (
                        "M.Tech. Software Engineering - MIS",
                        "M.Tech. Software Engineering - MIS",
                    ),
                    (
                        "Computer Science and Engineering with Specialisation in Business Analytics - MIA",
                        "Computer Science and Engineering with Specialisation in Business Analytics - MIA",
                    ),
                    ("Unauthorized", "Unauthorized"),
                ],
                max_length=500,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="role",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Program Representative", "Program Representative"),
                    ("Student", "Student"),
                    ("Head of Department", "Head of Department"),
                    ("Unauthorized", "Unauthorized"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="query",
            name="department",
            field=models.CharField(
                choices=[
                    (
                        "Computer Science & Engineering - BCE",
                        "Computer Science & Engineering - BCE",
                    ),
                    (
                        "Science and Engineering with Specialisation in Artificial Intelligence and Machine Learning - BAI",
                        "Science and Engineering with Specialisation in Artificial Intelligence and Machine Learning - BAI",
                    ),
                    (
                        "Computer Science and Engineering with Specialisation in Cyber Physical Systems - BPS",
                        "Computer Science and Engineering with Specialisation in Cyber Physical Systems - BPS",
                    ),
                    (
                        "Computer Science and Engineering with Specialisation in Artificial Intelligence and Robotics - BRS",
                        "Computer Science and Engineering with Specialisation in Artificial Intelligence and Robotics - BRS",
                    ),
                    (
                        "M.Tech. Software Engineering - MIS",
                        "M.Tech. Software Engineering - MIS",
                    ),
                    (
                        "Computer Science and Engineering with Specialisation in Business Analytics - MIA",
                        "Computer Science and Engineering with Specialisation in Business Analytics - MIA",
                    ),
                    ("Unauthorized", "Unauthorized"),
                ],
                max_length=200,
            ),
        ),
    ]