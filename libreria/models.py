from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    fundacion = models.PositiveIntegerField()
    sitio_web = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.pais})"

class Libro(models.Model):
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='libros')
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    precio = models.IntegerField()  # Monto en pesos

    def __str__(self):
        return self.titulo
