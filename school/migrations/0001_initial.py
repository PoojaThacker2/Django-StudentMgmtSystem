# Generated by Django 4.2 on 2023-07-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="School",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("city", models.CharField(max_length=100)),
                ("pin_code", models.CharField(max_length=10)),
                ("password", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=100)),
                ("username", models.CharField(max_length=50, unique=True)),
                ("password", models.CharField(max_length=255)),
                (
                    "grade",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Grade 1"),
                            (2, "Grade 2"),
                            (3, "Grade 3"),
                            (4, "Grade 4"),
                            (5, "Grade 5"),
                            (6, "Grade 6"),
                            (7, "Grade 7"),
                            (8, "Grade 8"),
                            (9, "Grade 9"),
                            (10, "Grade 10"),
                            (11, "Grade 11"),
                            (12, "Grade 12"),
                        ]
                    ),
                ),
            ],
        ),
    ]