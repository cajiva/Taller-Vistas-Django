from .logic.logic_measurements import get_all_measurements
from .logic.logic_measurements import get_measurement_id

from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json',measurements)
    return HttpResponse(measurements_list, content_type = 'application/json')


def get_measure(request):
    measurement = get_measurement_id(request)
    measurements_id = ('json',measurement)
    return HttpResponse(measurements_id, content_type = 'application/json')

