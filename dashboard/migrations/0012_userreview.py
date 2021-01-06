# Generated by Django 3.1.3 on 2021-01-06 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_delete_userreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('user_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboard.userprofilepicture')),
            ],
        ),
    ]
