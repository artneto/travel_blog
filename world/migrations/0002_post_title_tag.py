# Generated by Django 3.2 on 2022-02-19 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Hello world Blog!', max_length=255),
        ),
    ]
