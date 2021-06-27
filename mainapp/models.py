from django.db import models
from django.contrib.auth.models import User
import requests as r
from django.urls import reverse

# Create your models here.

def pokemon_list():
    listpokemons = []
    response = r.get('https://pokeapi.co/api/v2/pokemon/?limit=23')
    pokemons = response.json()
    for count, line in zip(range(len(pokemons['results'])), pokemons['results']):
        listpokemons.append((line['name'], line['name']))
    return listpokemons

POKEMON_CHOICES = pokemon_list()


# declaring a Student Model

class PokemonsList(models.Model):


    user = models.ForeignKey(User, on_delete=models.CASCADE, null='True', blank='True')
    name_pokemon = models.CharField(
        max_length=20,
        choices=POKEMON_CHOICES,
        default='1'
    )


    def __str__(self):
        return f'User: {self.user} | Pockemon: {self.name_pokemon}'
    def get_absolute_url(self):
        return reverse('profile')




