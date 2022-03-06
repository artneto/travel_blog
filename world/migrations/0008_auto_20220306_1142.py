# Generated by Django 3.2 on 2022-03-06 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0007_post_article_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='leader_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='article_snippet',
            field=models.CharField(default='', max_length=255),
        ),
    ]