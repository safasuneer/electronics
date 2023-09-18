
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    
    path('reg',UserRegView.as_view(),name="reg"),
    path('cus',CustomerView.as_view(),name="cus"),
    path('abo',AboutView.as_view(),name='abo'),
    path('con',ContactView.as_view(),name='con'),
    path('help',HelpView.as_view(),name='help'),
    path('pri',PricingView.as_view(),name='pri'),
    path('ser',ServiceView.as_view(),name='ser'),
    path('team',TeamView.as_view(),name='team'),
    path('pay',PaymentView.as_view(),name='pay'),
]