# Generated by Django 4.2.2 on 2023-06-20 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Student_app", "0001_initial"),
        ("Staff_app", "0001_initial"),
        ("HOD_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentfees",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="studentfees",
                to="Student_app.students",
            ),
        ),
        migrations.AddField(
            model_name="staffsalary",
            name="staff",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staffsalary",
                to="Staff_app.staffs",
            ),
        ),
    ]
