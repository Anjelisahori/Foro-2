from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Cien años de soledad'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Gabriel García Márquez'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Realismo mágico'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Breve sinopsis del libro'}),
        }
