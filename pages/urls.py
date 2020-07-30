from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePsgeView.as_view(), name='home')  # подключение страницы
]
