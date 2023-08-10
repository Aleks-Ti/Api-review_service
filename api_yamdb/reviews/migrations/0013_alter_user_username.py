# Generated by Django 3.2 on 2023-05-11 09:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('reviews', '0012_auto_20230511_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(
                max_length=150,
                null=True,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        regex='^[\\\\w.@+-]+\\\\Z'
                    )
                ],
            ),
        ),
    ]