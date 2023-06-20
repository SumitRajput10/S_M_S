# Generated by Django 4.2.2 on 2023-06-20 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("HOD_app", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="adminhod",
            name="admin",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
