# Generated by Django 2.1.5 on 2019-01-19 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_backend', '0008_auto_20190119_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_score', models.IntegerField(default=100)),
                ('shut_out_dice', models.IntegerField(default=1)),
                ('dice_numer', models.IntegerField(default=1)),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game_backend.Profile')),
            ],
        ),
    ]