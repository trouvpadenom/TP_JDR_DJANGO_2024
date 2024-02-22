from django.db import models

class Histoire(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()

    def __str__(self):
        return self.titre
