# Generated by Django 3.2 on 2023-05-09 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('reviews', '0002_category_genre_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='description',
        ),
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='titles',
                to='reviews.category',
            ),
        ),
    ]