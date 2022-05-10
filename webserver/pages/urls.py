from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index),
    path('KVP/', views.KVP),
    path('LawsofUI/', views.LawsofUI),
    path('ProductIA/', views.ProductIA),
]

urlpatterns += staticfiles_urlpatterns()