# Generated by Django 3.1.3 on 2021-01-01 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_userprofilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilepicture',
            name='profile_picture',
            field=models.ImageField(upload_to='dashboard/'),
        ),
    ]