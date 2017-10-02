from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView

from . import views

app_name = 'contestAnalyzer'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'Running/', views.process, name='process'),
    url(r'Main/', views.mainPage, name='mainPage'),
    url(r'Summary/', views.contestSummary, name='summary'),
    url(r'Log/', views.contestLog, name='log'),
]
