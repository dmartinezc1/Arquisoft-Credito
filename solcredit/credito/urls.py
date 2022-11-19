from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.creditos_view,name='variable_view'),
    path('<int:pk>', views.credito_view, name='variable_view'),
]