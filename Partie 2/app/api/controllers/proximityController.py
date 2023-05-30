from services.proximityService import ProximityService
from flask import jsonify

class ProximityController:
    def __init__(self):
        self.service = ProximityService()

    def get_proximitySensors(self):
        proximitySensors = self.service.get_proximitySensors()
        return jsonify(proximitySensors)
    
    def update_proximitySensor(self, proximitySensor_id, request):
        return self.service.update_proximitySensor(proximitySensor_id, request)

