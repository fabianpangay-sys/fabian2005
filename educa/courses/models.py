from django.db import models
from django.contrib.auth.models import User


# ------------------------
#   PERIODO
# ------------------------
class Periodo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre


# ------------------------
#   DOCENTE
# ------------------------
class Docente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


# ------------------------
#   ESTUDIANTE
# ------------------------
class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


# ------------------------
#   ASIGNATURA
# ------------------------
class Asignatura(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


# ------------------------
#   CURSO
# ------------------------
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    paralelo = models.CharField(max_length=5)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.paralelo} ({self.periodo})"


# ------------------------
#   CLASE
# ------------------------
class Clase(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.asignatura} - {self.curso} - {self.docente}"


# ------------------------
#   MATRICULA
# ------------------------
class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.estudiante} en {self.curso}"


class Nota(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    trimestre1 = models.FloatField(default=0)
    trimestre2 = models.FloatField(default=0)
    trimestre3 = models.FloatField(default=0)
    promedio = models.FloatField(default=0)

    def calcular_promedio(self):
        return round((self.trimestre1 + self.trimestre2 + self.trimestre3) / 3, 2)

    def save(self, *args, **kwargs):
        self.promedio = self.calcular_promedio()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Notas de {self.matricula.estudiante} ({self.asignatura})"
