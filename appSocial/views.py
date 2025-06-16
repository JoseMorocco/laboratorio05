from rest_framework import permissions, viewsets
from django.contrib.auth.models import Group, User
from .models import Usuario, Match, Mensaje, Cita, Cita_usuarios, Reseña
from .auth_serializers import UserSerializer, GroupSerializer
from .serializers import (
    UsuarioSerializer, MatchSerializer, 
    MensajeSerializer, CitaSerializer,
    CitaUsuariosSerializer, ReseñaSerializer
)
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class CitaUsuariosViewSet(viewsets.ModelViewSet):
    queryset = Cita_usuarios.objects.all()
    serializer_class = CitaUsuariosSerializer

class ReseñaViewSet(viewsets.ModelViewSet):
    queryset = Reseña.objects.all()
    serializer_class = ReseñaSerializer
