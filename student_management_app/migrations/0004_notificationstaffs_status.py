# Generated by Django 4.2.2 on 2023-07-03 12:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student_management_app", "0003_rename_course_subjects_course_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="notificationstaffs",
            name="status",
            field=models.IntegerField(default=0, null=True),
        ),
    ]
