# Generated by Django 4.0.1 on 2022-01-24 19:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_city_job_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]