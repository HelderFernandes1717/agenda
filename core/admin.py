from django.contrib import admin
from core.models import  Evento

# Register your models here.

##Listagem

class EventoAdmin(admin.ModelAdmin):
    list_display = ("id","titulo", "data_evento", "data_criacao")

admin.site.register(Evento, EventoAdmin)
