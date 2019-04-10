#Para registrar el modelo Perfil

from .models import Perfil
from django.contrib import admin 

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio', 'web')
