from django.db import models

class Credito(models.Model):
    name = models.CharField(max_length=50)
    valor = models.FloatField()
    empresa = models.CharField(max_length=10)
    fecha =models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10)

    def __str__(self):
        return '%s %s %s' % (self.name, self.valor, self.estado)
# Create your models here.
