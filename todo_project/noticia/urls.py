from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, AutorViewSet, NoticiaViewSet, ComentarioViewSet

# Criação do router
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'noticias', NoticiaViewSet)
router.register(r'comentarios', ComentarioViewSet)

# Inclusão das rotas no padrão de URLs
urlpatterns = [
    path('', include(router.urls)),
]
