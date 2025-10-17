# users/models.py

from django.db import models

class Usuario(models.Model):

    nombre1 = models.CharField(max_length=50)        # NOT NULL por defecto si no se usa null=True
    nombre2 = models.CharField(max_length=50, blank=True, null=True) # Se permite vacío
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    
    email = models.EmailField(max_length=200, unique=True)
    
    telefono = models.CharField(max_length=9) 
    
    def __str__(self):
        return self.email