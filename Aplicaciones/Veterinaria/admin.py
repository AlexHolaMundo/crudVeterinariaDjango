from django.contrib import admin
from .models import Raza,Pais,EstadoCivil,TipoAtencion,Medicamento, Propietario, Mascota, Atencion, Receta, Detalle
# Register your models here.
admin.site.register(Raza)
admin.site.register(Pais)
admin.site.register(EstadoCivil)
admin.site.register(TipoAtencion)
admin.site.register(Medicamento)
admin.site.register(Propietario)
admin.site.register(Mascota)
admin.site.register(Atencion)
admin.site.register(Receta)
admin.site.register(Detalle)