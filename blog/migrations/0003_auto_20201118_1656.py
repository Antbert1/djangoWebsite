# Generated by Django 3.1.3 on 2020-11-18 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FilePathField(default='postImage', path='blog/static/blog/img'),
        ),
    ]
