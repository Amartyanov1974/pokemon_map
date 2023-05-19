import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.timezone import localtime

from pokemon_entities.models import (Pokemon, PokemonEntity)


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent')


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    now_time = localtime()
    pokemon_entities = PokemonEntity.objects.filter(disappeared_at__gte=now_time,
                                                    appeared_at__lte=now_time)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        pokemon = pokemon_entity.pokemon
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri('/media/{}'.format(pokemon.image))
        )
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri('/media/{}'.format(pokemon.image)),
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemons = Pokemon.objects.all()
    now_time = localtime()
    for pokemon in pokemons:
        if pokemon.id == int(pokemon_id):
            requested_pokemon = pokemon
            break
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')
    pokemon_entities = PokemonEntity.objects.filter(pokemon=requested_pokemon)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_url = request.build_absolute_uri('/media/{}'.format(pokemon.image))

    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon_url
        )
    previous_evolution = None
    if pokemon.previous_evolution:
        previous_pokemon = pokemon.previous_evolution;
        previous_pokemon_url = request.build_absolute_uri('/media/{}'.format(previous_pokemon.image))
        previous_evolution = {'title_ru': previous_pokemon.title,
               'pokemon_id': previous_pokemon.id,
               'img_url': previous_pokemon_url,
               'description': previous_pokemon.description,
               'title_en': previous_pokemon.title_en,
               'title_jp': previous_pokemon.title_jp}
    try:
        next_pokemon = pokemon.next_evolution.get();
    except:
        next_pokemon = None
    next_evolution = None
    if next_pokemon:
        next_pokemon_url = request.build_absolute_uri('/media/{}'.format(next_pokemon.image))
        next_evolution = {'title_ru': next_pokemon.title,
               'pokemon_id': next_pokemon.id,
               'img_url': next_pokemon_url,
               'description': next_pokemon.description,
               'title_en': next_pokemon.title_en,
               'title_jp': next_pokemon.title_jp}

    pokemon = {'title_ru': pokemon.title,
               'pokemon_id': pokemon.id,
               'img_url': pokemon_url,
               'description': pokemon.description,
               'title_en': pokemon.title_en,
               'title_jp': pokemon.title_jp,
                'previous_evolution': previous_evolution,
                'next_evolution': next_evolution}
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
