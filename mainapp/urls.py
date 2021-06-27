from django.urls import path, include
from .views import *

urlpatterns = [
    path('', main_page, name='mainpage'),
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('profile/', get_profile , name='profile'),
    path('profile/add_pokemon/', AddPikaView.as_view() , name='add_pokemon'),
    path('pika_api/', PikaListView.as_view()),
    path("pika_api/<int:pk>/", PikaDetailView.as_view()),
]

