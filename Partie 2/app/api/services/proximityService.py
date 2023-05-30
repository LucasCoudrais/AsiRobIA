from repositories.genericRepository import GenericRepository
from flask import jsonify

class ProximityService:
    def __init__(self):
        self.repository = GenericRepository('data/proximity.json')

    def get_proximitySensors(self):
        return self.repository.read_entity()
    
    def update_proximitySensor(self, proximitySensor_id, request):
        updated_proximitySensor = request.get_json()
        proximitySensors = self.repository.read_entity()

        for proximitySensor in proximitySensors:
            if proximitySensor['id'] == proximitySensor_id:
                proximitySensor.update(updated_proximitySensor)
                self.repository.write_entity(proximitySensors)
                return jsonify(proximitySensor), 200
        
        return jsonify({'message': 'Capteur de proximité non trouvé'}), 404

