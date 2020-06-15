# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Agent(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    code = models.CharField(max_length=100,null=True)
    def __unicode__(self):
        return "{0} [{1}]".format(self.num, self.email,self.first_name, self.last_name, self.code)

class Task(models.Model):
    idtask= models.CharField(max_length=255, unique=True)
    statut = models.CharField(max_length=30, blank=True)
    idAgent = models.ForeignKey(Agent,on_delete=models.CASCADE,)
    title = models.CharField(max_length=30, blank=True)
    date_debut = models.CharField(max_length=255,null=True)
    date_fin = models.CharField(max_length=255,null=True)
    def __unicode__(self):
        return "{0} [{1}] [{2}]".format(self.num, self.idtask,self.statut,self.idAgent.num, self.title,self.date_debut, self.date_fin)