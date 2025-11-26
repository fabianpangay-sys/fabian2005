from django.contrib import admin
from .models import (
    Periodo,
    Docente,
    Estudiante,
    Asignatura,
    Curso,
    Clase,
    Matricula,
    Nota
)


@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "fecha_inicio", "fecha_fin")
    search_fields = ("nombre",)


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ("user", "titulo", "telefono")
    search_fields = ("user__username", "user__first_name", "user__last_name")


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("user", "cedula", "fecha_nacimiento")
    search_fields = ("cedula", "user__username", "user__first_name")



@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "paralelo", "periodo")
    list_filter = ("periodo",)
    search_fields = ("nombre", "paralelo")


@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ("asignatura", "curso", "docente")
    list_filter = ("curso", "asignatura", "docente")



@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ("estudiante", "curso", "periodo", "fecha")
    list_filter = ("periodo", "curso")
    search_fields = ("estudiante__user__username", "estudiante__cedula")


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ("matricula", "asignatura", "trimestre1", "trimestre2", "trimestre3", "promedio")
    list_filter = ("asignatura",)
    search_fields = ("matricula__estudiante__user__username",)
