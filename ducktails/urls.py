from django.urls import path
from .views import *

urlpatterns = [
  path('', DuckHomePageView.as_view(), name='duck_home'),
  path('home', DuckHomePageView.as_view(), name='home'),
  path('about', DuckAboutPageView.as_view(), name='duck_about'),
  path('list', DuckListPageView.as_view(), name='duck_list'),
  path('<int:pk>/', DuckDetailPageView.as_view(), name='duck_detail'),
  path('<int:pk>/update/', DuckUpdateView.as_view(), name='duck_update'),
  path('create/', DuckCreateView.as_view(), name='duck_create'),
  path('<int:pk>/delete/', DuckDeleteView.as_view(), name='duck_delete'),
]