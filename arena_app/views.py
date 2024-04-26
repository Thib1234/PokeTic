from rest_framework import viewsets
from .models import Badge, Arene
from .serializers import BadgeSerializer, AreneSerializer


class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer


class AreneViewSet(viewsets.ModelViewSet):
    queryset = Arene.objects.all()
    serializer_class = AreneSerializer
