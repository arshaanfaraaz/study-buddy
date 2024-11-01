# Generated by Django 5.1.1 on 2024-11-01 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_student_student_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReportCard",
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
                ("student_rank", models.IntegerField()),
                ("date_of_generation", models.DateField(auto_now=True)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="studentreportcard",
                        to="core.student",
                    ),
                ),
            ],
        ),
    ]