from services.tempService import TempService
from flask import jsonify

class TempController:
    def __init__(self):
        self.service = TempService()

    def get_tempSensors(self):
        tempSensors = self.service.get_tempSensors()
        return jsonify(tempSensors)
    
    def update_tempSensor(self, tempSensor_id, request):
        return self.service.update_tempSensor(tempSensor_id, request)

