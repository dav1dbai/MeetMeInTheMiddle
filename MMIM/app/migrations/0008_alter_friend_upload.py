# Generated by Django 3.2.20 on 2023-11-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_friend_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='upload',
            field=models.ImageField(default='NULL', upload_to='media/'),
        ),
    ]