from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, MatchViewSet, MensajeViewSet, CitaViewSet, CitaUsuariosViewSet, ReseñaViewSet, UserViewSet,GroupViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'matchs', MatchViewSet)
router.register(r'mensajes', MensajeViewSet)
router.register(r'citas', CitaViewSet)
router.register(r'cita_usuarios', CitaUsuariosViewSet)
router.register(r'reseñas', ReseñaViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
