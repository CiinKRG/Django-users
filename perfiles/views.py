#Aquí hacemos uso de las vistas basadas en clase
#este archivo depende (esta conctado) con urls.py y models.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Perfil
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView

#Con el CreateView, Django automaticamente buscará por todo el proyecto la carpeta templates un archivo
#llamado app_form o en este caso perfil_form.html (se usaría en caso de que necesitemos crear una parte
#de edición donde los usuarios puedan actualizar su perfil)

class SignInView(LoginView):
    template_name = 'perfiles/iniciar_sesion.html'

class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm
    def form_valid(self, form):
        #En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate
        #para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'perfiles/bienvenida.html'

#Solo nos cerrará la sesión
class SignOutView(LogoutView):
    pass
