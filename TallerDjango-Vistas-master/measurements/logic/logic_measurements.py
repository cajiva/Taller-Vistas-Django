from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement_id(id):
    measure = Measurement.objects.get(id)
    return measure