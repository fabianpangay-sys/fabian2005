from django.db import models

class Hardware(models.Model):
    nombre = models.CharField(max_length=150)
    numero_serie = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    fecha_adquisicion = models.DateField()
    ubicacion = models.CharField(max_length=150)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.numero_serie})"


class Falla(models.Model):
    equipo = models.ForeignKey(Hardware, on_delete=models.CASCADE)
    fecha_reporte = models.DateTimeField()
    descripcion = models.TextField()
    prioridad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Falla en {self.equipo}"


class Mantenimiento(models.Model):
    falla = models.ForeignKey(Falla, on_delete=models.CASCADE)
    tecnico = models.CharField(max_length=120)  # Simplificado
    tipo_mantenimiento = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    trabajo_realizado = models.TextField()

    def __str__(self):
        return f"Mantenimiento de {self.falla}"
