# Generated by Django 2.2.24 on 2023-05-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_pokemonentity_pokemon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Lat',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Lon',
            new_name='lon',
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]