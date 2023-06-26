# Generated by Django 4.2.2 on 2023-06-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student_management_app", "0002_customuser_profile_pic"),
    ]

    operations = [
        migrations.RenameField(
            model_name="subjects",
            old_name="course",
            new_name="course_id",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="profile_pic",
            field=models.ImageField(
                default="{% url static '/assets/img/profiles/default_avatar.jpg' %}",
                upload_to="media/profile_pic",
            ),
        ),
    ]
