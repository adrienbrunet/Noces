#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


class Inscrits(models.Model):
    FamilyName			= models.CharField(max_length=255)
    NbPersonneFamille   = models.IntegerField()
    PresenceNoce        = models.BooleanField()
    PresenceFeteFamille = models.BooleanField()

    def __unicode__(self):
                return str(self.FamilyName)

class Transport(models.Model):
    Nom      = models.CharField(max_length=255)
    Nombre   = models.IntegerField(null=True)
    Ville    = models.CharField(max_length=255,null=True)
    Date     = models.CharField(max_length=255,null=True)
    Contact  = models.CharField(max_length=255,null=True)
    Remarque = models.CharField(max_length=255,null=True)

    def __unicode__(self):
        return str(self.Nom)
