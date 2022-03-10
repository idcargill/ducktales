from pyexpat import model
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import DuckModel

class DuckHomePageView(TemplateView):
  template_name   = 'duck_home.html'
  model           = DuckModel

class DuckAboutPageView(TemplateView):
  template_name   = 'duck_about.html'
  model           = DuckModel

class DuckListPageView(ListView):
  template_name   = 'duck_list.html'
  model           = DuckModel

class DuckDetailPageView(DetailView):
  template_name   = 'duck_detail.html'
  model           = DuckModel
  
class DuckCreateView(CreateView):
  template_name   = 'forms/duck_create.html'
  model           = DuckModel
  fields          = [ 'name', 'species', 'is_laying', 'age', 'owner' ]
  
  
class DuckUpdateView(UpdateView):
  template_name   = 'forms/duck_update.html'
  model           = DuckModel
  fields          = [ 'name', 'species', 'is_laying', 'age', 'owner' ] 

  
class DuckDeleteView(DeleteView):
  template_name   = 'forms/duck_delete.html'
  model           = DuckModel


class DuckHomeView(TemplateView):
  template_name   = 'duck_home.html'
  model           = DuckModel
