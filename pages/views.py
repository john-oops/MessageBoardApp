from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


# Create your views here.
class HomePsgeView(ListView):  # отображение бд на домашней страницы
    model = Post
    template_name = 'home.html'
