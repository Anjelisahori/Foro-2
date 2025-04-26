from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('agregar/', views.agregar_libro, name='agregar_libro'),
    path('editar/<int:pk>/', views.editar_libro, name='editar_libro'),
    path('eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),
    path('externos/', views.libros_externos, name='libros_externos'),  # ← NUEVO
    path('reservar/', views.reservar_libro, name='reservar_libro'),

]
