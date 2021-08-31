from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement_id(id):
    measure = Measurement.objects.get(pk=id)
    return measure

def delete_measurement_id(id):
    Measurement.objects.filter(pk=id).delete()

def update_measurement_id(id,val):
    Measurement.objects.filter(pk=id).update(value=val)
    