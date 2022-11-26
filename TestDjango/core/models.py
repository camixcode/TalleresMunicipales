from django.db import models

# Create your models here.


class Material(models.Model):
    idMaterial = models.AutoField(primary_key=True, verbose_name='Id de material')
    nombreMaterial = models.CharField(max_length=50, verbose_name='Nombre de material')
    descripcionMaterial = models.CharField(max_length=50, verbose_name='Descripcion de material')
    stock = models.IntegerField(verbose_name='Stock de material')

    def __str__(self):
        return self.nombreMaterial
