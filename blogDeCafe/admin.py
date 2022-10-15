from django.contrib import admin
from blogDeCafe.models import Entrada, Curso

# Register your models here.
class EntradaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "imagen")

class CursoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha", "precio", "cupos", "imagen")
    list_filter = ("fecha", "precio")
    date_hierarchy = "fecha"

admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Curso, CursoAdmin)
