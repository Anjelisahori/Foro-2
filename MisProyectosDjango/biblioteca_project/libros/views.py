from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm
from django.http import HttpResponse
from .models import Reserva


def lista_libros(request):
    libros = Libro.objects.all()
    reservas = Reserva.objects.all().order_by('-fecha_reserva')  # ordenadas por fecha
    return render(request, 'libros/lista_libros.html', {'libros': libros, 'reservas': reservas})
def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/agregar_libro.html', {'form': form})

def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/editar_libro.html', {'form': form})

def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'libros/eliminar_libro.html', {'libro': libro})
import requests  # Importa requests arriba de todo

def libros_externos(request):
    response = requests.get('https://gutendex.com/books/')
    if response.status_code == 200:
        data = response.json()
        libros = data['results']  # Aquí vienen los libros de la API
    else:
        libros = []
    return render(request, 'libros/libros_externos.html', {'libros': libros})
def reservar_libro(request):
    titulo = request.GET.get('titulo', 'Título desconocido')
    return render(request, 'libros/reserva_exitosa.html', {'titulo': titulo})
def reservar_libro(request):
    titulo = request.GET.get('titulo', 'Título desconocido')
    # Guardar la reserva en la base de datos
    Reserva.objects.create(titulo=titulo)
    return render(request, 'libros/reserva_exitosa.html', {'titulo': titulo})
