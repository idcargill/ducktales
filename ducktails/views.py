from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import DuckModel
from django.urls import reverse_lazy

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
  fields          = [ 'name', 'species', 'is_laying', 'age', 'notes', 'owner' ]
  success_url     = reverse_lazy('duck_list')
  
  
class DuckUpdateView(UpdateView):
  template_name   = 'forms/duck_update.html'
  model           = DuckModel
  fields          = [ 'name', 'species', 'is_laying', 'age', 'notes', 'owner' ] 
  success_url     = reverse_lazy('duck_list')
  
class DuckDeleteView(DeleteView):
  template_name   = 'forms/duck_delete.html'
  model           = DuckModel
  success_url     = reverse_lazy('duck_list')

class DuckHomeView(TemplateView):
  template_name   = 'duck_home.html'
  model           = DuckModel
