# Generated by Django 3.2 on 2023-05-09 23:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('reviews', '0009_remove_user_username_is_not_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]