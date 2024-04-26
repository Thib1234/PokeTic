from rest_framework import viewsets
from .models import Joueur
from .serializers import JoueurSerializer


class JoueurViewSet(viewsets.ModelViewSet):
    queryset = Joueur.objects.all()
    serializer_class = JoueurSerializer
