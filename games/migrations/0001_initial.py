# Generated by Django 3.1.5 on 2021-01-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_img', models.ImageField(upload_to='images/')),
                ('main_img', models.ImageField(upload_to='images/')),
                ('name_img', models.ImageField(upload_to='images/')),
                ('alt_text', models.CharField(max_length=50)),
                ('game_title', models.CharField(max_length=50)),
                ('game_description', models.TextField()),
                ('release_date', models.DateField(verbose_name='')),
                ('publisher_1', models.CharField(max_length=50)),
                ('publisher_1_anchor', models.URLField()),
                ('publisher_2', models.CharField(blank=True, max_length=50)),
                ('publisher_2_anchor', models.URLField(blank=True)),
                ('publisher_3', models.CharField(blank=True, max_length=50)),
                ('publisher_3_anchor', models.URLField(blank=True)),
                ('trailer_url', models.URLField()),
                ('platform_1', models.CharField(max_length=20)),
                ('platform_1_anchor', models.URLField()),
                ('platform_2', models.CharField(blank=True, max_length=20)),
                ('platform_2_anchor', models.URLField(blank=True)),
                ('platform_3', models.CharField(blank=True, max_length=20)),
                ('platform_3_anchor', models.URLField(blank=True)),
            ],
        ),
    ]
