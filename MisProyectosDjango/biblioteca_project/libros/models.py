from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
class Reserva(models.Model):
    titulo = models.CharField(max_length=255)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo