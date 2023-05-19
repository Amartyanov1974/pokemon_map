# Generated by Django 3.1.14 on 2023-05-19 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_pokemonentity_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemonentity',
            name='description',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]