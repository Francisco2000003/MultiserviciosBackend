from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServicioViewSet

# Creamos un router y registramos nuestro ViewSet
router = DefaultRouter()
router.register(r'servicios', ServicioViewSet)

# Incluimos las URLs generadas por el router
urlpatterns = [
    path('', include(router.urls)),
]
