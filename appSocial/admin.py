from django.contrib import admin

# Register your models here.
from .models import Usuario, Match, Mensaje, Cita, Cita_usuarios, Reseña

admin.site.register(Usuario)
admin.site.register(Match)
admin.site.register(Mensaje)
admin.site.register(Cita)
admin.site.register(Cita_usuarios)
admin.site.register(Reseña)
