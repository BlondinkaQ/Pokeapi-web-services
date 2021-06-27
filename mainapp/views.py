from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserLoginForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from .models import PokemonsList, POKEMON_CHOICES


from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, ProfileSerializer

# Create your views here.

def main_page(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Успішна регестрація!')
            return redirect('login')
        else:
            messages.error(request, 'Некоректно введені дані.')
    else:
        form = UserCreationForm()
    return render(request, 'reg_page.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'login_form': form})

def log_out(request):
    logout(request)
    return redirect('login')

def get_profile(request):
    list_user = PokemonsList.objects.filter(user=request.user).values('name_pokemon')
    name_list_usable = []
    for i in list(list_user):
        name_list_usable.append(i['name_pokemon'])
        #name_list_usable.append(POKEMON_CHOICES[int(i['name_pokemon'])-1][1])
    return render(request, 'profile.html', {'user': request.user, 'list_user' : name_list_usable})



class AddPikaView(CreateView):
    model = PokemonsList
    template_name = 'add_pokemon.html'
    fields = ['name_pokemon']


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PikaListView(APIView):
    """Вивод списка покемонів"""
    def get(self, request):
        pikas = PokemonsList.objects.all()
        serializer = ProfileSerializer(pikas, many=True)
        return Response(serializer.data)


class PikaDetailView(APIView):
    """Вивод по user"""
    def get(self, request, pk):
        pikas = PokemonsList.objects.filter(user_id=pk)
        serializer = ProfileSerializer(pikas, many=True)
        return Response(serializer.data)
