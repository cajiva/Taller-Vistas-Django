from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('variables/', include('variables.urls')),
    path('measurements/', include('measurements.urls')),
    path('measurements/id', include('measurements.urls')),
    
]
