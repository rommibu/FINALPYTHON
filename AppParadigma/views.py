from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from AppParadigma.models import Entrada, Comentario
from .models import Seccional, Autos, Avatar
from AppParadigma.forms import ComentarioForm, FormularioFamilia, AutosFormu, UserEditForm, AvatarForm, FormularioInteres
from AppParadigma import views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, PostForm
from django.views.generic import ListView, DetailView


def seccional(request):
    seccional1=Seccional(nombre="Alberdi", seccional=3)
    seccional.save()
    seccional2=Seccional(nombre="Centro", seccional=1)
    seccional2.save()
    lista=[seccional1, seccional2]
    return render(request, "AppParadigma/seccional.html", {"listado":lista, "imagen":obtenerAvatar(request)})


def inicio(request):
    posts=Post.objects.all()
    context = {'posts': posts}
    return render(request, "AppParadigma/inicio.html", context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm (request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('inicio')
    else:
        form = UserRegisterForm()
        
    context = { 'form':form }
    return render(request, 'AppParadigma/register.html', context)

@login_required
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post enviado')
            #return redirect('inicio')
    else:
        form = PostForm()
    return render(request, 'AppParadigma/post.html', {'form': form})


def profile(request, username=None):
    current_user=request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, "AppParadigma/profile.html", {'user':user, 'posts':posts})


def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f'sigues a {username}')
    return redirect('inicio')


def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	messages.success(request, f'Ya no sigues a {username}')
	return redirect('inicio')


def asociado(request):
    if request.method == "POST":
        miFormulario = FormularioFamilia(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            print(info)
            nombre = info.get("nombre")
            apellido = info.get("apellido")
            dni = info.get("dni")
            extranjero = info.get("extranjero")
            mail = info.get("mail")
            familia = Asociado(nombre=nombre, apellido=apellido, dni=dni,extranjero=extranjero, mail=mail)
            familia.save()
            return render(request, "AppParadigma/asociado.html", {"mensaje": "Tu informacion quedo registrada!", "imagen":obtenerAvatar(request)})
        else:
            return render(request, "AppParadigma/asociado.html", {"mensaje": "Ingreso algun dato incorrecto, por favor verifique!", "imagen":obtenerAvatar(request)})
    else:
        miFormulario = FormularioFamilia()
        return render(request, "AppParadigma/asociado.html", {"formulario": miFormulario, "imagen":obtenerAvatar(request)})

def caracteristicas(request):
    if request.method == "POST":
            miInteres = FormularioInteres(request.POST)
            print(miInteres)
            if miInteres.is_valid():
                info = miInteres.cleaned_data
                print(info)
                asociado=info.get("asociado")
                codigo=info.get("codigo")
                fecha_creacion=info.get("fecha_creacion")
                intereses=info.get("intereses") 
                gustos = Caracteristicas(asociado=asociado, codigo=codigo, fecha_creacion=fecha_creacion, intereses=intereses)
                gustos.save()
                return render(request, "AppParadigma/caracteristicas.html", {"mensaje": "Tu informacion quedo registrada!", "imagen":obtenerAvatar(request)})
            else:
                return render(request, "AppParadigma/caracteristicas.html", {"mensaje": "Ingreso algun dato incorrecto, por favor verifique!", "imagen":obtenerAvatar(request)})
    else:
        miInteres = FormularioInteres()
        return render(request, "AppParadigma/caracteristicas.html", {"formulario": miInteres, "imagen":obtenerAvatar(request)})           
            
        
    

def conocenos(request):
    return render(request, "AppParadigma/conocenos.html")

def inicio(request):
    articulos = Entrada.objects.all()
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data ['nombre']
            comentario = form.cleaned_data ['comentario']
            obj = Comentario(nombre=nombre, comentario=comentario)
            obj.save()
            mensaje = "GRACIAS POR TU COMENTARIO"
        return render(request, "AppParadigma/post.html",{"articulos":articulos, "mensaje":mensaje, "form":form, "imagen":obtenerAvatar(request)})
    form = ComentarioForm()
    return render(request, "AppParadigma/post.html", {"articulos":articulos, "form":form})



def leerAsociado(request):
    asociados=Asociado.objects.all()
    print(asociados)
    return render (request, "AppParadigma/leerAsociado.html", {"asociados":asociados, "imagen":obtenerAvatar(request)})

def leerCaracteristicas(request):
    asociados=Caracteristicas.objects.all()
    print(caracteristicas)
    return render (request, "AppParadigma/leerCaracteristicas.html", {"caracteristicas":caracteristicas, "imagen":obtenerAvatar(request)})


def busquedaAsociado(request):
    return render(request, "AppParadigma/resultadoBusqueda.html", {"imagen":obtenerAvatar(request)})

def eliminarAsociado(request, id):
    family=Asociado.objects.get(id=id)
    family.delete()
    asociados=Asociado.objects.all()
    return render(request, "AppParadigma/leerAsociado.html", {"asociados":asociados, "imagen":obtenerAvatar(request)})


def editarAsociado(request, id):
    family=Asociado.objects.get(id=id)
    if request.method=="POST":
        form=FormularioFamilia(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            family.nombre=info["nombre"]
            family.apellido=info["nombre"]
            family.dni=info["dni"]
            family.extranjero=info["extranjero"]
            family.mail=info["mail"]
            family.save()
            asociados=Asociado.objects.all()
            return render(request, "AppParadigma/leerAsociado.html", {"asociados":asociados, "imagen":obtenerAvatar(request)})
    else:
        form=FormularioFamilia(initial={"nombre":family.nombre, "apellido":family.apellido, "dni":family.dni, "extranjero":family.extranjero, "mail":family.mail, "id":family.id, "imagen":obtenerAvatar(request)})
        return render(request, "AppParadigma/editarAsociado.html", {"formulario":form, "dni_Asociado":family.dni, "imagen":obtenerAvatar(request)})


def escuderia(request):
    if request.method == "POST":
        miFormue = AutosFormu(request.POST)
        print(miFormue)
        if miFormue.is_valid():
            info1 = miFormue.cleaned_data
            print(info1)
            id = info1.get("id")
            nombre = info1["nombre"]
            escuderias = info1["escuderias"]
            piloto = info1["piloto"]
            auto = Autos(id, nombre, escuderias, piloto)
            auto.save()
            return render(request, "AppParadigma/inicio.html", {"mensaje": "Exelecente ya estas participando!", "imagen":obtenerAvatar(request)})
        else:
            return render(request, "AppParadigma/escuderias.html", {"mensaje": "Error", "imagen":obtenerAvatar(request)})

    else:
        miFormue = AutosFormu()
        return render(request, "AppParadigma/escuderias.html", {"formularioc": miFormue, "imagen":obtenerAvatar(request)})


def busquedaescu(request):
    return render(request, "AppMVT/resultadoevento.html", {"imagen":obtenerAvatar(request)})

def Buscar(request):
    if request.GET["nombre"]:

        persona = request.GET["nombre"]
        personas = Autos.objects.filter(nombre=persona)

        if len(personas) != 0:

            return render(request, "AppParadigma/busquedaevento.html", {"personas": personas, "imagen":obtenerAvatar(request)})

        else:
            return render(request, "AppParadigma/busquedaevento.html", {"mensaje": "No figurar como registrado, Vamos!! registrate para el evento!!", "imagen":obtenerAvatar(request)})
    else:
        return render (request, "AppParadigma/resultadoevento.html",{"mensaje": "No figurar como registrado, Vamos!! registrate para el evento!!", "imagen":obtenerAvatar(request)})

#@login_request
def editarProfile(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario.first_name=form.cleaned_data["fist_name"]
            usuario.last_name=form.cleaned_data["last_name"]
            usuario.email=form.cleaned_data["email"]
            usuario.password1=form.cleaned_data["password1"]
            usuario.password2=form.cleaned_data["password"]
            usuario.save()
            return render(request, 'AppParadigma', {'mensaje':f"Perfil de {usuario} ya editado"})
    else:
        form= UserEditForm(instance=usuario)
    return render(request, 'AppParadigma/editarProfile.html', {'form':form, usuario:'usuario',"imagen":obtenerAvatar(request)})

#@login_request
def agregarAvatar(request):
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)>0):
                avatarViejo.delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'AppParadigma', {'usuario':request.user, 'mensaje':'LISTO TU AVATAR!'})
    else:
        formulario=AvatarForm()
    return render(request, 'AppParadigma/agregarAvatar.html', {'form':formulario, 'usuario':request.user, "imagen":obtenerAvatar(request)})


def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="Paradigma\media\avatares\batman.png"
    return imagen


class SeccionalList(ListView):
    model = Seccional 
    template_name = 'AppParadigma/leerSeccional.html' 

class SeccionalDetalle(DetailView):
    model=Seccional
    template_name='AppParadigma/detalleSeccional.html'
    
def leerSeccional(request):
    secciones=Seccional.objects.all()
    print(secciones)
    return render (request, "AppParadigma/leerSeccional.html", {"nombre":nombre})