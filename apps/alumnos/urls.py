from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("nuevo/", views.alumno_create, name="alumno_create"),
]
