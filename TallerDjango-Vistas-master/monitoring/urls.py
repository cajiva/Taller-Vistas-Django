from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('variables/', include('variables.urls')),
    path('measurements/', include('measurements.urls')),
    path('measurements/<int:id>/', include('measurements.urls')),
    path('measurements/delete/<int:id>/', include('measurements.urls')),
    path('measurements/update/<int:id>/<int:val>/', include('measurements.urls')),
]
