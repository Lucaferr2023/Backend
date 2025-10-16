# users/urls.py

from django.urls import path
from .views import UsuarioListCreate

urlpatterns = [
    # Esta ruta mapeará a /api/usuarios/
    path('usuarios/', UsuarioListCreate.as_view(), name='usuario-list-create'),
]

