from django.contrib import admin
from django.urls import path
from auth_app import views
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('accueil/', views.accueil, name='accueil'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('histoire/', include('histoire.urls')),
]
