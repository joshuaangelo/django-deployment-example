# Generated by Django 4.0.1 on 2022-02-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.FileField(blank=True, upload_to='profile_pics'),
        ),
    ]