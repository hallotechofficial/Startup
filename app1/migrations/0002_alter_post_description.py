# Generated by Django 5.0.1 on 2024-03-10 04:41

import django.core.exceptions
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="description",
            field=models.TextField(verbose_name=django.core.exceptions.ValidationError),
        ),
    ]
