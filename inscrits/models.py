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
