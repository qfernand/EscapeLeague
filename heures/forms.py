# -*- coding: utf-8 -*-
# coding: utf8
from __future__ import unicode_literals

from django import forms
from django.utils import timezone
from django.forms.models import inlineformset_factory
from heures import models

class PersonneForm( forms.ModelForm ) :
    class Meta : 
        model = models.Personne
        exclude = ['id']