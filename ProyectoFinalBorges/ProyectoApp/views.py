from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from ProyectoApp.models import *
from ProyectoApp.forms import *
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
def inicioSesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contrasenia)

            if user:
                login(request, user)
                return render(request, "ProyectoApp/inicio.html", {"mensaje" : f"Bienvenido {user}"})
        else:
            return render (request, "ProyectoApp/login.html", {"mensaje":"Datos incorrectos,refresque la pagina e intente nuevamente"})
    else:
        form = AuthenticationForm()
    return render(request, "ProyectoApp/login.html", {"Formulario": form})

def registro(request):
    if request.method == "POST":
        form = UsuarioRegistro(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render (request, "ProyectoApp/inicio.html", {"mensaje":"Usuario creado con exito!"})
    else:
         form = UsuarioRegistro()
    return render(request, "ProyectoApp/registro.html", {"Formulario": form})     

@login_required
def editarUsuario(request):
    usuario = request.user
    if request.method == "POST":

        form = FormEdit(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render (request, "ProyectoApp/inicio.html")
    else:
        form = FormEdit(initial = {"email":usuario.email, "first_name":usuario.first_name, "last_name":usuario.last_name})

    return render(request, "ProyectoApp/editarUsuario.html", {"Formulario": form, "usuario": usuario})    


def inicio(request):
    return render(request,"ProyectoApp/inicio.html")

def maquillaje(request):
    return render(request,"ProyectoApp/maquillajes.html")

def accesorio(request):
    return render(request,"ProyectoApp/accesorios.html")

def usuario(request):
    return render(request,"ProyectoApp/usuarios.html")

def cremasFaciales(request):
    return render(request,"ProyectoApp/cremasFaciales.html")

def about(request):
    return render(request,"ProyectoApp/about.html")

def busquedaNombreMaquillaje(request):
    return render(request, "ProyectoApp/inicio.html")

def resultadosBusqueda(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        listaMaquillajes = Maquillaje.objects.filter(nombre__contains=nombre)

        return render(request, "ProyectoApp/inicio.html", {"listaMaquillajes":listaMaquillajes, "nombre": nombre})
    else:
        respuesta = "No enviaste Datos"
    return HttpResponse(respuesta)

@login_required
def agregarAvatar(request):
    if request.method =="POST":
        form = Avatarform(request.POST, request.FILES)

        if form.is_valid():
            usuarioAct = User.objects.get(username = request.user)

            avatar= Avatar(usuario=usuarioAct, imagen = form.cleaned_data["imagen"])
        avatar.save()
        return render(request, "ProyectoApp/inicio.html")
    else:
        form = Avatarform()
    return render (request, "ProyectoApp/agregarAvatar.html", {"Formulario": form})    


#Crud Maquillajes

class ListaMaquillaje(ListView):
    model = Maquillaje

class DetalleMaquillaje(DetailView):
    model = Maquillaje

class CrearMaquillaje(LoginRequiredMixin,CreateView):
    model = Maquillaje
    
    success_url = "/ProyectoApp/maquillaje/list"
    fields = {"nombre","imagen", "color", "precio", "descripcion"}

class EditarMaquillaje(LoginRequiredMixin,UpdateView):
    model = Maquillaje
    success_url = "/ProyectoApp/maquillaje/list"
    fields = {"nombre","imagen", "color", "precio", "descripcion"}

class EliminarMaquillaje(LoginRequiredMixin,DeleteView):
    model = Maquillaje
    success_url = "/ProyectoApp/maquillaje/list"

#crud Accesorios

class ListaAccesorios(ListView):
    model = Accesorio

class DetalleAccesorios(DetailView):
    model = Accesorio

class CrearAccesorio(LoginRequiredMixin,CreateView):
    model = Accesorio
    
    success_url = "/ProyectoApp/accesorio/list"
    fields = {"nombre","imagen", "color", "precio", "descripcion"}

class EditarAccesorio(LoginRequiredMixin,UpdateView):
    model = Accesorio
    success_url = "/ProyectoApp/accesorio/list"
    fields = {"nombre","imagen", "color", "precio", "descripcion"}

class EliminarAccesorio(LoginRequiredMixin,DeleteView):
    model = Accesorio
    success_url = "/ProyectoApp/accesorio/list"

#crud Cremas faciales

class ListaCremasFaciales(ListView):
    model = CremasFaciales

class DetalleCremaFacial(DetailView):
    model = CremasFaciales

class CrearCremaFacial(LoginRequiredMixin,CreateView):
    model = CremasFaciales
    
    success_url = "/ProyectoApp/cremasFaciales/list"
    fields = {"nombre","imagen", "precio", "descripcion"}

class EditarCremaFacial(LoginRequiredMixin,UpdateView):
    model = CremasFaciales
    success_url = "/ProyectoApp/cremasFaciales/list"
    fields = {"nombre","imagen", "precio", "descripcion"}

class EliminarCremaFacial(LoginRequiredMixin,DeleteView):
    model = CremasFaciales
    success_url = "/ProyectoApp/cremasFaciales/list"

#crud Cremas Corporales

class ListaCremasCorporales(ListView):
    model = CremasCorporales

class DetalleCremaCorporal(DetailView):
    model = CremasCorporales

class CrearCremaCorporal(LoginRequiredMixin,CreateView):
    model = CremasCorporales
    
    success_url = "/ProyectoApp/cremasCorporales/list"
    fields = {"nombre","imagen", "precio", "descripcion"}

class EditarCremaCorporal(LoginRequiredMixin,UpdateView):
    model = CremasCorporales
    success_url = "/ProyectoApp/cremasCorporales/list"
    fields = {"nombre","imagen", "precio", "descripcion"}

class EliminarCremaCorporal(LoginRequiredMixin,DeleteView):
    model = CremasCorporales
    success_url = "/ProyectoApp/cremasCorporales/list"    
   