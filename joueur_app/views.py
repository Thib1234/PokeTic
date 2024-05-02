from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Joueur
from .serializers import JoueurSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


class JoueurViewSet(viewsets.ModelViewSet):
    queryset = Joueur.objects.all()
    serializer_class = JoueurSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user = User.objects.create_user(username=data['username'], password=data['password'])
        data['user'] = user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        joueur = self.request.user.joueur
        data = {
            'username': joueur.user.username,  # Accéder au username du User associé
            'argent': joueur.argent,
            'pokemons': list(joueur.pokemons.values()),
            # Ajoutez d'autres champs si nécessaire
        }
        return JsonResponse(data)


