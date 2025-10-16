# users/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer
from django.core.mail import send_mail # Importar la función de correo

# Vista para Listar y Crear Usuarios (GET y POST)
class UsuarioListCreate(APIView):
    def get(self, request):
        """ Consultar la lista de usuarios registrados. [cite: 30] """
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ Crear un usuario ingresando Nombre, Email y Teléfono.  """
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            user_instance = serializer.save()
            
            # 1. Enviar la notificación por correo electrónico 
            self.send_notification(user_instance)
            
            # 2. Devolver la respuesta JSON [cite: 37]
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_notification(self, user_instance):
        """ Función que envía una notificación por correo electrónico al crearse el usuario.  """
        subject = f'Nuevo Usuario Registrado: {user_instance.nombre1}'
        message = (f'Se ha creado un nuevo usuario en el sistema.\n\n'
                   f'Detalles:\n'
                   f'Nombre: {user_instance.nombre1} {user_instance.apellido1}\n'
                   f'Email: {user_instance.email}\n'
                   f'Teléfono: {user_instance.telefono}')
        
        # Dirección del administrador o la que deba recibir la notificación
        admin_email = 'administrador@ejemplo.com' 
        
        try:
            send_mail(
                subject,
                message,
                # Usa la dirección configurada como remitente en settings.py
                'servidor@tudominio.com', 
                [admin_email],
                fail_silently=False,
            )
            print(f"Notificación enviada a {admin_email} por el nuevo usuario: {user_instance.email}")
        except Exception as e:
            print(f"Error al enviar la notificación: {e}")
