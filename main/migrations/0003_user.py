# Generated by Django 3.2 on 2021-05-12 05:57

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_traindetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(default=None, max_length=255)),
                ('name', models.CharField(default=None, max_length=255, null=True)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to=main.models.user_directory_path)),
            ],
        ),
    ]
