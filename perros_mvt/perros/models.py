from django.db import models

class Perro(models.Model):
    nombre = models.CharField(max_length = 255)
    descripcion = models.TextField()
    imagen = models.URLField()
    temperamento = models.CharField(max_length = 255)
    origen = models.CharField(max_length = 255, default = "", blank = True)
    otros_nombres = models.CharField(max_length = 255, default = "", blank = True)

    def __str__(self):
        return self.nombre
