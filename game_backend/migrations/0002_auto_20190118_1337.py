# Generated by Django 2.1.5 on 2019-01-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='designed_game_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='game_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='win_count',
            field=models.IntegerField(default=0),
        ),
    ]