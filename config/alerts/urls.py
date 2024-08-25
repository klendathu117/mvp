from django.urls import path
from . import views

urlpatterns = [
    #path('view-a/', views.view_a, name='view_a'),
    path('templates/create/', views.create_template, name='create_template'),
    path('templates/', views.list_templates, name='list_templates'),
    path('map/', views.map_alert, name='map_alert'),
    path('mappings/', views.view_mappings, name='view_mappings'),
    path('home/', views.home, name='home'),
]