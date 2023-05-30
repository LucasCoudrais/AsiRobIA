from repositories.genericRepository import GenericRepository
from flask import jsonify

class InteruptorService:
    def __init__(self):
        self.repository = GenericRepository('data/interuptor.json')

    def get_interuptors(self):
        return self.repository.read_entity()
    
    def update_interuptor(self, interuptor_id, request):
        updated_interuptor = request.get_json()
        interuptors = self.repository.read_entity()

        for interuptor in interuptors:
            if interuptor['id'] == interuptor_id:
                interuptor.update(updated_interuptor)
                self.repository.write_entity(interuptors)
                return jsonify(interuptor), 200
        
        return jsonify({'message': 'Intérupteur non trouvé'}), 404

