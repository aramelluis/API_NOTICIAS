from rest_framework import viewsets
from .models import Categoria, Autor, Noticia, Comentario
from .serializers import CategoriaSerializer, AutorSerializer, NoticiaSerializer, ComentarioSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar e editar categorias.
    Fornece automaticamente as operações 'list', 'create', 'retrieve',
    'update' e 'destroy'.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class AutorViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar e editar autores.
    Fornece automaticamente as operações 'list', 'create', 'retrieve',
    'update' e 'destroy'.
    """
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class NoticiaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar e editar notícias.
    Fornece automaticamente as operações 'list', 'create', 'retrieve',
    'update' e 'destroy'.
    """
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar e editar comentários.
    Fornece automaticamente as operações 'list', 'create', 'retrieve',
    'update' e 'destroy'.
    """
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
