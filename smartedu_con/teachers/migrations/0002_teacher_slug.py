# Generated by Django 3.2.9 on 2021-11-17 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
