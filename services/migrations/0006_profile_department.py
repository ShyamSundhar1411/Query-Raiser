# Generated by Django 4.1.1 on 2022-10-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0005_rename_raisedquery_query"),
    ]

    operations = [
        migrations.AddField(
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
                ],
                max_length=500,
                null=True,
            ),
        ),
    ]
