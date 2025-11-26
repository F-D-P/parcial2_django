from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('crear/', views.alumno_create, name='alumno_create'),
    path('<int:id>/detalle/', views.alumno_detail, name='alumno_detail'),
    path('<int:id>/editar/', views.alumno_update, name='alumno_update'),
    path('<int:id>/eliminar/', views.alumno_delete, name='alumno_delete'),
]
