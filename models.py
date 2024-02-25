from django.contrib.auth.models import AbstractUser
from django.db import models
class Utilisateur(AbstractUser):


    nom = models.CharField(max_length=100, unique=True)
    mot_de_passe = models.CharField(max_length=100)
    cpt_mort = models.IntegerField(default=0)

       
    def __str__(self):
        return self.nom