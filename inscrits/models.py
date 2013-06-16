#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


class Inscrits(models.Model):
    FamilyName			= models.CharField(max_length=255)
    NbPersonneFamille   = models.CharField(max_length=255)
    PresenceNoce        = models.IntegerField()
    PresenceFeteFamille = models.IntegerField()
