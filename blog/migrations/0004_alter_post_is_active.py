# Generated by Django 4.2 on 2024-01-11 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
