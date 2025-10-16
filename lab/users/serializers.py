# users/serializers.py


from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'email', 'telefono']



