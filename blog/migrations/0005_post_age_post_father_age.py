# Generated by Django 4.2 on 2024-01-11 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_post_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="age",
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="father_age",
            field=models.SmallIntegerField(null=True),
        ),
    ]
