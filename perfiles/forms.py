#Aquí se tiene el formulario para que los usuarios se registren
#from django import forms
from django.contrib.auth.forms import UserCreationForm
#, AuthenticationForm
from django.contrib.auth.models import User
#from .models import Perfil

class SignUpForm(UserCreationForm):

#Aquí se ponen los campos que contenga el formulario
    class Meta:
        model = User
        fields = (
                'username',
                'first_name',
                'password1',
                'password2',
                )
