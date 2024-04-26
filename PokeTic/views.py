from django.shortcuts import render

from joueur_app.models import Joueur


def index(request):
    joueur = Joueur.objects.get(nom='thib')

    return render(request, 'landing_page.html', {'joueur': joueur})
