from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from .models import Periodo, Docente, Estudiante, Asignatura, Curso, Clase, Matricula, Nota
from django.contrib.auth.models import User


# ================================
#   CRUD Periodo
# ================================
class PeriodoListView(ListView):
    model = Periodo
    template_name = "calificaciones/periodo_list.html"
    context_object_name = "periodos"


class PeriodoCreateView(CreateView):
    model = Periodo
    fields = ["nombre", "fecha_inicio", "fecha_fin"]
    template_name = "calificaciones/periodo_form.html"
    success_url = reverse_lazy("periodo_list")


class PeriodoUpdateView(UpdateView):
    model = Periodo
    fields = ["nombre", "fecha_inicio", "fecha_fin"]
    template_name = "calificaciones/periodo_form.html"
    success_url = reverse_lazy("periodo_list")


class PeriodoDeleteView(DeleteView):
    model = Periodo
    template_name = "calificaciones/periodo_delete.html"
    success_url = reverse_lazy("periodo_list")


class PeriodoDetailView(DetailView):
    model = Periodo
    template_name = "calificaciones/periodo_detail.html"



# ================================
#   CRUD Docente
# ================================
class DocenteListView(ListView):
    model = Docente
    template_name = "calificaciones/docente_list.html"
    context_object_name = "docentes"


class DocenteCreateView(CreateView):
    model = Docente
    fields = ["user", "titulo", "telefono"]
    template_name = "calificaciones/docente_form.html"
    success_url = reverse_lazy("docente_list")


class DocenteUpdateView(UpdateView):
    model = Docente
    fields = ["user", "titulo", "telefono"]
    template_name = "calificaciones/docente_form.html"
    success_url = reverse_lazy("docente_list")


class DocenteDeleteView(DeleteView):
    model = Docente
    template_name = "calificaciones/docente_delete.html"
    success_url = reverse_lazy("docente_list")


class DocenteDetailView(DetailView):
    model = Docente
    template_name = "calificaciones/docente_detail.html"



# ================================
#   CRUD Estudiante
# ================================
class EstudianteListView(ListView):
    model = Estudiante
    template_name = "calificaciones/estudiante_list.html"
    context_object_name = "estudiantes"


class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = ["user", "cedula", "fecha_nacimiento", "direccion"]
    template_name = "calificaciones/estudiante_form.html"
    success_url = reverse_lazy("estudiante_list")


class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = ["user", "cedula", "fecha_nacimiento", "direccion"]
    template_name = "calificaciones/estudiante_form.html"
    success_url = reverse_lazy("estudiante_list")


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = "calificaciones/estudiante_delete.html"
    success_url = reverse_lazy("estudiante_list")


class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = "calificaciones/estudiante_detail.html"



# ================================
#   CRUD Asignatura
# ================================
class AsignaturaListView(ListView):
    model = Asignatura
    template_name = "calificaciones/asignatura_list.html"
    context_object_name = "asignaturas"


class AsignaturaCreateView(CreateView):
    model = Asignatura
    fields = ["nombre"]
    template_name = "calificaciones/asignatura_form.html"
    success_url = reverse_lazy("asignatura_list")


class AsignaturaUpdateView(UpdateView):
    model = Asignatura
    fields = ["nombre"]
    template_name = "calificaciones/asignatura_form.html"
    success_url = reverse_lazy("asignatura_list")


class AsignaturaDeleteView(DeleteView):
    model = Asignatura
    template_name = "calificaciones/asignatura_delete.html"
    success_url = reverse_lazy("asignatura_list")


class AsignaturaDetailView(DetailView):
    model = Asignatura
    template_name = "calificaciones/asignatura_detail.html"



# ================================
#   CRUD Curso
# ================================
class CursoListView(ListView):
    model = Curso
    template_name = "calificaciones/curso_list.html"
    context_object_name = "cursos"


class CursoCreateView(CreateView):
    model = Curso
    fields = ["nombre", "paralelo", "periodo"]
    template_name = "calificaciones/curso_form.html"
    success_url = reverse_lazy("curso_list")


class CursoUpdateView(UpdateView):
    model = Curso
    fields = ["nombre", "paralelo", "periodo"]
    template_name = "calificaciones/curso_form.html"
    success_url = reverse_lazy("curso_list")


class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "calificaciones/curso_delete.html"
    success_url = reverse_lazy("curso_list")


class CursoDetailView(DetailView):
    model = Curso
    template_name = "calificaciones/curso_detail.html"



# ================================
#   CRUD Clase
# ================================
class ClaseListView(ListView):
    model = Clase
    template_name = "calificaciones/clase_list.html"
    context_object_name = "clases"


class ClaseCreateView(CreateView):
    model = Clase
    fields = ["docente", "asignatura", "curso"]
    template_name = "calificaciones/clase_form.html"
    success_url = reverse_lazy("clase_list")


class ClaseUpdateView(UpdateView):
    model = Clase
    fields = ["docente", "asignatura", "curso"]
    template_name = "calificaciones/clase_form.html"
    success_url = reverse_lazy("clase_list")


class ClaseDeleteView(DeleteView):
    model = Clase
    template_name = "calificaciones/clase_delete.html"
    success_url = reverse_lazy("clase_list")


class ClaseDetailView(DetailView):
    model = Clase
    template_name = "calificaciones/clase_detail.html"



# ================================
#   CRUD Matrícula
# ================================
class MatriculaListView(ListView):
    model = Matricula
    template_name = "calificaciones/matricula_list.html"
    context_object_name = "matriculas"


class MatriculaCreateView(CreateView):
    model = Matricula
    fields = ["estudiante", "curso", "periodo", "fecha"]
    template_name = "calificaciones/matricula_form.html"
    success_url = reverse_lazy("matricula_list")


class MatriculaUpdateView(UpdateView):
    model = Matricula
    fields = ["estudiante", "curso", "periodo", "fecha"]
    template_name = "calificaciones/matricula_form.html"
    success_url = reverse_lazy("matricula_list")


class MatriculaDeleteView(DeleteView):
    model = Matricula
    template_name = "calificaciones/matricula_delete.html"
    success_url = reverse_lazy("matricula_list")


class MatriculaDetailView(DetailView):
    model = Matricula
    template_name = "calificaciones/matricula_detail.html"



# ================================
#   CRUD Nota
# ================================
class NotaListView(ListView):
    model = Nota
    template_name = "calificaciones/nota_list.html"
    context_object_name = "notas"


class NotaCreateView(CreateView):
    model = Nota
    fields = ["matricula", "asignatura", "trimestre1", "trimestre2", "trimestre3"]
    template_name = "calificaciones/nota_form.html"
    success_url = reverse_lazy("nota_list")


class NotaUpdateView(UpdateView):
    model = Nota
    fields = ["matricula", "asignatura", "trimestre1", "trimestre2", "trimestre3"]
    template_name = "calificaciones/nota_form.html"
    success_url = reverse_lazy("nota_list")


class NotaDeleteView(DeleteView):
    model = Nota
    template_name = "calificaciones/nota_delete.html"
    success_url = reverse_lazy("nota_list")


class NotaDetailView(DetailView):
    model = Nota
    template_name = "calificaciones/nota_detail.html"
