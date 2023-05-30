from repositories.genericRepository import GenericRepository
from flask import jsonify

class TempService:
    def __init__(self):
        self.repository = GenericRepository('data/temperature.json')

    def get_tempSensors(self):
        return self.repository.read_entity()
    
    def update_tempSensor(self, tempSensor_id, request):
        updated_tempSensor = request.get_json()
        tempSensors = self.repository.read_entity()

        for tempSensor in tempSensors:
            if tempSensor['id'] == tempSensor_id:
                tempSensor.update(updated_tempSensor)
                self.repository.write_entity(tempSensors)
                return jsonify(tempSensor), 200
        
        return jsonify({'message': 'Capteur de température non trouvé'}), 404

