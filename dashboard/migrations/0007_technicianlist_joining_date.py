# Generated by Django 3.1.3 on 2020-12-28 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_technicianlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='technicianlist',
            name='joining_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
