# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Exists
from django.contrib.admin.utils import get_deleted_objects
from django.utils.datastructures import MultiValueDictKeyError
from django.template.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.defaulttags import register
from django.forms.models import inlineformset_factory
from django.views.generic import UpdateView, DeleteView, DetailView
from django.urls import reverse, reverse_lazy
from datetime import datetime    
from heures import models
from heures import forms

def index(request):
    personnes = models.Personne.objects.all()
    print(personnes)
    return render(request, 'heures/index.html', {'liste_personnes': personnes})

def adminPersonne(request):
    noPersonne = False
    personnes = models.Personne.objects.all()
    print(personnes)
    return render(request, 'heures/adminPersonne.html', locals())

def nouvellePersonne(request):
    form = forms.PersonneForm(request.POST or None)
    if form.is_valid():
        form.save()
    else :
        return render(request, 'heures/nouvellePersonne.html', 
                          {'form': form})
    return redirect('/heures/adminPersonne')
    
    return render(request, 'heures/nouvellePersonne.html', locals())
class deletePersonne(DeleteView):  # Une vue basée sur une classe, qui dérive de la classe générique DeleteView de Django pour supprimer une P_Physique existante
	template_name = 'heures/deletePersonne.html'
	model = models.Personne
	context_object_name = 'Personne'

	def get_context_data(self, **kwargs): # fonction qui retrace toutes les références de l'objet passé en paramètre et renvoi le tout dans context
		context = super(DeleteView,self).get_context_data(**kwargs)
		return context

	success_url = reverse_lazy('adminPersonne')

# Create your views here.
