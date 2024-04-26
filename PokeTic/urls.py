from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemon_app/', include('pokemon_app.urls')),
    path('combat_app/', include('combat_app.urls')),
    path('dresseur_app/', include('dresseur_app.urls')),
    path('joueur_app/', include('joueur_app.urls')),
    path('object_app/', include('object_app.urls')),
    path('arena_app/', include('arena_app.urls')),

]
