from django.urls import path
from . import views

urlpatterns = [
    path('', views.scraper_form, name='scraper_form'),
    path('enviar/', views.scraper_enviar, name='scraper_enviar'),
]
