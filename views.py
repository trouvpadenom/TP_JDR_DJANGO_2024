from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


from auth_app.models import Utilisateur

@login_required
def mort(request):
    # Récupérer l'utilisateur actuel par son nom d'utilisateur
    utilisateur = request.user
    # Mettre à jour le compteur de pages de mort pour l'utilisateur actuel
    utilisateur.cpt_mort += 1
    utilisateur.save()
    return render(request, 'mort.html')

@login_required
def victoire(request):
    # Essayez de récupérer l'utilisateur actuel s'il existe
    try:
        utilisateur = request.user
    except Utilisateur.DoesNotExist:
        # Si l'utilisateur n'existe pas, renvoyez une réponse appropriée
        return HttpResponse("Utilisateur non trouvé dans la base de données.")

    # Si l'utilisateur existe, récupérez le compteur de pages de mort
    cpt_mort = utilisateur.cpt_mort
    return render(request, 'victoire.html', {'cpt_mort': cpt_mort})


def chap1(request):
    return render(request, 'chap1.html')

def chap2(request):
    return render(request, 'chap2.html')

def chap3(request):
    return render(request, 'chap3.html')

