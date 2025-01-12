# Generated by Django 3.1.14 on 2023-05-19 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0018_auto_20230519_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Имя покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity', to='pokemon_entities.pokemon', verbose_name='Покемон'),
        ),
    ]
