# Generated by Django 3.1.3 on 2020-11-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201118_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FilePathField(default='postImage', path='blog/static/img'),
        ),
    ]
