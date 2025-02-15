# Generated by Django 5.0.1 on 2024-01-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_anime_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='episodes',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='my_episode',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='anime',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='animetype',
            name='name',
            field=models.CharField(max_length=63),
        ),
    ]
