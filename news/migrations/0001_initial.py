# Generated by Django 3.1.5 on 2021-01-16 14:01

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('excerpt', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
