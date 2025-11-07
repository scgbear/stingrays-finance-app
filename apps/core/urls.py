from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('investment-calculator/', views.investment_calculator, name='investment_calculator'),
]