from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django.forms import ModelForm
from .models import *

class ComentarioForm(forms.Form):
    nombre= forms.CharField(label='Nombre:', max_length=60)
    comentario = forms.CharField (widget=forms.Textarea)
    
    
class AutosFormu(ModelForm):
    class Meta:
        model = Autos
        fields = "__all__"
        

class FormularioFamilia(forms.Form):
    nombre=forms.CharField(max_length=60)
    apellido=forms.CharField(max_length=60)
    dni=forms.FloatField()
    extranjero=forms.BooleanField()
    mail=forms.EmailField()
    
class FormularioInteres(forms.Form):
    asociado=models.CharField(max_length=60)
    codigo=models.IntegerField()
    fecha_creacion=models.DateField()
    intereses=models.TextField(max_length=600) 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'username': 'Nombre completo', 'email': 'Agrega tu mail'}
        help_texts = { k:"" for k in fields }


class AutenticarForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')
        

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label='Modificar E-mail')
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    firstName=forms.CharField(label='Modificar Nombre')
    lastName=forms.CharField(label='Modificar Apellido')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}
        
class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': '¿Qué está pasando?'}), required=True)
    
    class Meta:
        model = Post
        fields = ['content']
        
class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")
