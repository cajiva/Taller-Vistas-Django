from django.urls import path
from . import views

urlspatterns = [
    path('list/', views.get_variables, name = 'variableList')
]
