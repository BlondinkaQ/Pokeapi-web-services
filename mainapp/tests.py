from .models import POKEMON_CHOICES
from django.contrib.auth.forms import UserCreationForm
from django.test import TestCase


class UserCreationFormTest(TestCase):

    def test_register(self):
        data = {'username': 'user1'}
        form = UserCreationForm(data)
        self.assertTrue(form.is_valid())

        data['password'] = 'Try_password_1'
        form = UserCreationForm(data)
        self.assertTrue(form.is_valid())

class ChoosePokemonTest(TestCase):

    def test_pika(self):
        pokemon_1 = POKEMON_CHOICES[0]
        pokemon_2 = POKEMON_CHOICES[1]
        assert pokemon_1[0] == 'bulbasaur'
        assert pokemon_2[1] == 'ivysaur'







