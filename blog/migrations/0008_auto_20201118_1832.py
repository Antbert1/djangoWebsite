# Generated by Django 3.1.3 on 2020-11-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201118_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(default='defaultImage', upload_to='img'),
        ),
    ]