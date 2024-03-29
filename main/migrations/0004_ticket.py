# Generated by Django 3.0.3 on 2021-06-11 12:48

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100, null=True)),
                ('train_no', models.CharField(max_length=10)),
                ('date', models.CharField(default=None, max_length=100, null=True)),
                ('passenger_name', models.CharField(max_length=100, null=True)),
                ('uid', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField()),
                ('image', models.FileField(blank=True, null=True, upload_to=main.models.user_directory_path)),
            ],
        ),
    ]
