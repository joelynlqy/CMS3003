from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('map/', views.map, name='map'),
    path('new_incident/', views.new_incident_form, name='new_incident_form')
]