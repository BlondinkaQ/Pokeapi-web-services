from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import PokemonsList

from django.contrib.auth.models import User, auth

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model =   PokemonsList
        fields = "__all__"





