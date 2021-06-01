# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import re # regular expression pour le validate_siret

from django.contrib.admin.utils import NestedObjects
from django.utils.text import capfirst
from django.utils.encoding import force_str

class Personne(models.Model):
	id = models.AutoField(primary_key = True)
	CIVILITE_CHOICES = (
		('F', 'Mme.'),
		('H', 'M.'),
	)
	civilite = models.CharField(max_length=5, choices=CIVILITE_CHOICES)
	nom = models.CharField(max_length=25)
	prenom = models.CharField(max_length=30)


	def __unicode__(self):
			return u''.join(self.prenom.encode('utf-8') + " "+ self.nom.upper().encode('utf-8'))
	def __str__(self):
			return u''.join(self.prenom.decode('utf-8') + " "+ self.nom.upper().decode('utf-8'))
	def save(self, *args, **kwargs):
		if isinstance(self.nom, str):
			self.nom=self.nom.decode("utf-8")
		if isinstance(self.prenom, str):
			self.prenom=self.prenom.decode("utf-8")
		return super(Personne, self).save(*args, **kwargs)
