from django.urls import path
from . import views

urlspatterns = [
    path('list/', views.get_measurements, name = 'measurementsList'),
    path('id/', views.get_measure(id), name = 'measurementsId'),
]