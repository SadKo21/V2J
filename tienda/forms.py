from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3 , max_length=50)
    precio = forms.IntegerField(min_value=1, max_value=30000)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este Nombre Ya Existe")

        return nombre

    class Meta:
        model = Producto
        fields = "__all__"

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password2"]