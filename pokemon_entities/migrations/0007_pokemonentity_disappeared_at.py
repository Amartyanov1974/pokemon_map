# Generated by Django 2.2.24 on 2023-05-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20230518_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
