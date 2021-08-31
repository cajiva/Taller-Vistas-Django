from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name = 'measurementsList'),
    path('<int:id>/', views.get_measure, name = 'measurementsId'),
    path('delete/<int:id>/', views.delete_measure, name = 'measurementsDelete'),
    path('update/<int:id>/<int:val>/', views.update_measure, name = 'measurementsUpdate'),
]