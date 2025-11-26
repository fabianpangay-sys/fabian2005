from django.urls import path
from .views import (
    PeriodoListView, PeriodoCreateView, PeriodoUpdateView, PeriodoDeleteView, PeriodoDetailView,
    DocenteListView, DocenteCreateView, DocenteUpdateView, DocenteDeleteView, DocenteDetailView,
    EstudianteListView, EstudianteCreateView, EstudianteUpdateView, EstudianteDeleteView, EstudianteDetailView,
    AsignaturaListView, AsignaturaCreateView, AsignaturaUpdateView, AsignaturaDeleteView, AsignaturaDetailView,
    CursoListView, CursoCreateView, CursoUpdateView, CursoDeleteView, CursoDetailView,
    ClaseListView, ClaseCreateView, ClaseUpdateView, ClaseDeleteView, ClaseDetailView,
    MatriculaListView, MatriculaCreateView, MatriculaUpdateView, MatriculaDeleteView, MatriculaDetailView,
    NotaListView, NotaCreateView, NotaUpdateView, NotaDeleteView, NotaDetailView
)

urlpatterns = [

    # ----------------- PERIODO -----------------
    path("periodos/", PeriodoListView.as_view(), name="periodo_list"),
    path("periodos/nuevo/", PeriodoCreateView.as_view(), name="periodo_create"),
    path("periodos/<int:pk>/editar/", PeriodoUpdateView.as_view(), name="periodo_update"),
    path("periodos/<int:pk>/eliminar/", PeriodoDeleteView.as_view(), name="periodo_delete"),
    path("periodos/<int:pk>/", PeriodoDetailView.as_view(), name="periodo_detail"),

    # ----------------- DOCENTE -----------------
    path("docentes/", DocenteListView.as_view(), name="docente_list"),
    path("docentes/nuevo/", DocenteCreateView.as_view(), name="docente_create"),
    path("docentes/<int:pk>/editar/", DocenteUpdateView.as_view(), name="docente_update"),
    path("docentes/<int:pk>/eliminar/", DocenteDeleteView.as_view(), name="docente_delete"),
    path("docentes/<int:pk>/", DocenteDetailView.as_view(), name="docente_detail"),

    # ----------------- ESTUDIANTE -----------------
    path("estudiantes/", EstudianteListView.as_view(), name="estudiante_list"),
    path("estudiantes/nuevo/", EstudianteCreateView.as_view(), name="estudiante_create"),
    path("estudiantes/<int:pk>/editar/", EstudianteUpdateView.as_view(), name="estudiante_update"),
    path("estudiantes/<int:pk>/eliminar/", EstudianteDeleteView.as_view(), name="estudiante_delete"),
    path("estudiantes/<int:pk>/", EstudianteDetailView.as_view(), name="estudiante_detail"),

    # ----------------- ASIGNATURA -----------------
    path("asignaturas/", AsignaturaListView.as_view(), name="asignatura_list"),
    path("asignaturas/nuevo/", AsignaturaCreateView.as_view(), name="asignatura_create"),
    path("asignaturas/<int:pk>/editar/", AsignaturaUpdateView.as_view(), name="asignatura_update"),
    path("asignaturas/<int:pk>/eliminar/", AsignaturaDeleteView.as_view(), name="asignatura_delete"),
    path("asignaturas/<int:pk>/", AsignaturaDetailView.as_view(), name="asignatura_detail"),

    # ----------------- CURSO -----------------
    path("cursos/", CursoListView.as_view(), name="curso_list"),
    path("cursos/nuevo/", CursoCreateView.as_view(), name="curso_create"),
    path("cursos/<int:pk>/editar/", CursoUpdateView.as_view(), name="curso_update"),
    path("cursos/<int:pk>/eliminar/", CursoDeleteView.as_view(), name="curso_delete"),
    path("cursos/<int:pk>/", CursoDetailView.as_view(), name="curso_detail"),

    # ----------------- CLASE -----------------
    path("clases/", ClaseListView.as_view(), name="clase_list"),
    path("clases/nuevo/", ClaseCreateView.as_view(), name="clase_create"),
    path("clases/<int:pk>/editar/", ClaseUpdateView.as_view(), name="clase_update"),
    path("clases/<int:pk>/eliminar/", ClaseDeleteView.as_view(), name="clase_delete"),
    path("clases/<int:pk>/", ClaseDetailView.as_view(), name="clase_detail"),

    # ----------------- MATRICULA -----------------
    path("matriculas/", MatriculaListView.as_view(), name="matricula_list"),
    path("matriculas/nuevo/", MatriculaCreateView.as_view(), name="matricula_create"),
    path("matriculas/<int:pk>/editar/", MatriculaUpdateView.as_view(), name="matricula_update"),
    path("matriculas/<int:pk>/eliminar/", MatriculaDeleteView.as_view(), name="matricula_delete"),
    path("matriculas/<int:pk>/", MatriculaDetailView.as_view(), name="matricula_detail"),

    # ----------------- NOTA -----------------
    path("notas/", NotaListView.as_view(), name="nota_list"),
    path("notas/nuevo/", NotaCreateView.as_view(), name="nota_create"),
    path("notas/<int:pk>/editar/", NotaUpdateView.as_view(), name="nota_update"),
    path("notas/<int:pk>/eliminar/", NotaDeleteView.as_view(), name="nota_delete"),
    path("notas/<int:pk>/", NotaDetailView.as_view(), name="nota_detail"),
]
