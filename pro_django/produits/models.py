from django.db import models

# Create your models here.

class Produit(models.Model):
    nom = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    prix = models.DecimalField(max_digits=10000, decimal_places=2)
    active = models.BooleanField()
    live = models.BooleanField()
    is_delete = models.BooleanField(null=True)
