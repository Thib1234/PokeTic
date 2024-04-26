from rest_framework import viewsets
from .models import PNJ, Ligue
from .serializers import PNJSerializer, LigueSerializer


class PNJViewSet(viewsets.ModelViewSet):
    queryset = PNJ.objects.all()
    serializer_class = PNJSerializer


class LigueViewSet(viewsets.ModelViewSet):
    queryset = Ligue.objects.all()
    serializer_class = LigueSerializer
