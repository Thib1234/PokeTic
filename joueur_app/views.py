from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Joueur
from .serializers import JoueurSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


class JoueurViewSet(viewsets.ModelViewSet):
    queryset = Joueur.objects.all()
    serializer_class = JoueurSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        data['password'] = make_password(data['password'])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'])
    @login_required
    def me(self, request):
        joueur = request.user.joueur
        data = {
            'nom': joueur.nom,
            'argent': joueur.argent,
            'pokemons': list(joueur.pokemons.values()),
        }
        return JsonResponse(data)
