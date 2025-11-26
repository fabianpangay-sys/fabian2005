from django.contrib import admin
from .models import Hardware, Falla, Mantenimiento

admin.site.register(Hardware)
admin.site.register(Falla)
admin.site.register(Mantenimiento)
