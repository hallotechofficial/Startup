# Generated by Django 5.0.1 on 2024-03-10 04:43

import app1.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0002_alter_post_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="description",
            field=models.TextField(verbose_name=[app1.models.validate_min_words]),
        ),
    ]
