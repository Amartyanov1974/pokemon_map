from django.db import models


class Pokemon(models.Model):
    title = models.CharField('Имя покемона', max_length=200, blank=True)
    title_en = models.CharField('Имя на английском языке', max_length=200, blank=True)
    title_jp = models.CharField('Имя на японском языке', max_length=200, blank=True)
    image = models.ImageField('Картинка', upload_to='pokemons',
                              blank=True, null=True)
    previous_evolution = models.ForeignKey('self', on_delete=models.CASCADE,
                                           blank=True, null=True,
                                           verbose_name='Предыдущая эволюция',
                                           related_name='next_evolution')
    description = models.TextField('Описание',blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон',
                                on_delete=models.CASCADE)
    lat = models.FloatField('Широта', blank=True, null=True)
    lon = models.FloatField('Долгота', blank=True, null=True)
    appeared_at = models.DateTimeField('Появится в', blank=True, null=True)
    disappeared_at = models.DateTimeField('Исчезнет в', blank=True, null=True)
    level = models.IntegerField('Уровень', blank=True, null=True)
    health = models.IntegerField('Здоровье', blank=True, null=True)
    strength = models.IntegerField('Сила', blank=True, null=True)
    defence = models.IntegerField('Защита', blank=True, null=True)
    stamina = models.IntegerField('Выносливость', blank=True, null=True)
