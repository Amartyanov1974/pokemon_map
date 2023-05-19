# Generated by Django 2.2.24 on 2023-05-18 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_pokemon_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lat', models.FloatField(blank=True, null=True)),
                ('Lon', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
