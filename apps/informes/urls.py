from django.urls import path
from . import views

urlpatterns = [
    path("enviar/<int:id>/", views.enviar_pdf, name="enviar_pdf"),
]
