from typing import Type
from django.db import models
from django.db import connection
from datetime import *
from django.core.exceptions import ValidationError
from django.db.models.options import Options
import json

# Pour vider toutes les donnees d'une table
# with connection.cursor() as cursor:
#     cursor.execute("DELETE FROM dall_diamm_restaurant")


# Create your models here.
class connexion (models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    email=models.EmailField()
    Tel=models.CharField(max_length=50)
    confirmationmdp = models.CharField(max_length=8)
    motdepasse = models.CharField(max_length=8)
    