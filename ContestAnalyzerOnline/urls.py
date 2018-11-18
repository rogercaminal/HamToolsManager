from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView

from . import views

app_name = 'contestAnalyzer'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'Running/', views.process, name='process'),
    url(r'Main/', views.main_page, name='mainPage'),
    url(r'Summary/', views.contest_summary, name='summary'),
    url(r'Log/', views.contest_log, name='log'),
    url(r'Rates/', views.contest_rates, name='rates'),
    url(r'RatePerMin/', views.contest_rates_per_minute, name='ratepermin'),
    url(r'DXCCFrequency/', views.contest_dxcc_frequency, name='dxccfreq'),
    url(r'Charts/', views.contest_plots, name='plots'),
    url(r'Maps/', views.maps, name='maps'),
    url(r'GuestBook/', views.guestbook, name='guestbook'),
]
