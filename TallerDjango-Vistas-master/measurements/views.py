from .logic.logic_measurements import *


from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json',measurements)
    return HttpResponse(measurements_list, content_type = 'application/json')

def get_measure(request,id):
    measurement = get_measurement_id(id)
    return HttpResponse(measurement, content_type = 'application/json')

def delete_measure(request,id):
    delete_measurement_id(id)
    return HttpResponse("<int:id> deleted")

def update_measure(request,id,val):
    update_measurement_id(id,val)
    return HttpResponse("<int:id> updated")
