from rest_framework import viewsets
from .models import TypeObjet, Objet
from .serializers import TypeObjetSerializer, ObjetSerializer


class TypeObjetViewSet(viewsets.ModelViewSet):
    queryset = TypeObjet.objects.all()
    serializer_class = TypeObjetSerializer


class ObjetViewSet(viewsets.ModelViewSet):
    queryset = Objet.objects.all()
    serializer_class = ObjetSerializer
