from rest_framework import viewsets
from .models import Combat
from .serializers import CombatSerializer


class CombatViewSet(viewsets.ModelViewSet):
    queryset = Combat.objects.all()
    serializer_class = CombatSerializer
