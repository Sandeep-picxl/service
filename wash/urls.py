from django.urls import pathfrom . import viewsurlpatterns = [    path('', views.main, name="main"),    path('service_detail', views.service_detail, name="service_detail"),    path('service_create', views.service_create, name="service_create"),    path('send_message', views.send_message, name='send_message'),    path('about', views.about, name="about"),]