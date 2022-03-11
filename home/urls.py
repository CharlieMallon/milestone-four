# pylint: disable=missing-module-docstring
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('manage_shop/', views.manage_shop, name='manage_shop'),
]
