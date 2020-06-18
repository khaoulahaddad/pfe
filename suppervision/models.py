# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from django.db import models

# Create your models here.
class Agent(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    code = models.CharField(max_length=100,null=True)
    code_carte = models.CharField(max_length=100, blank=True)
    def __unicode__(self):
        return "{0} [{1}]".format(self.num, self.email,self.first_name, self.last_name, self.code, code.code_carte,',')

class Product(models.Model):
    idProduct= models.CharField(max_length=255, unique=True)
    statut = models.CharField(max_length=30, blank=True)
    adresse = models.CharField(max_length=30, blank=True)
    date_commande = models.DateTimeField(default=date.today() ,max_length=255, null= True)
    date_livraison = models.DateTimeField(default=date.today() ,max_length=255, null= True)
    date_recu = models.DateTimeField(default=date.today(), max_length=255, null= True)
    def __unicode__(self):
        return "{0} [{1}] [{2}]".format(self.num, self.idProduct,self.statut, self.adresse,self.date_commande, self.date_livraison, self.date_recu)