from services.interuptorService import InteruptorService
from flask import jsonify

class InteruptorController:
    def __init__(self):
        self.service = InteruptorService()

    def get_interuptors(self):
        interuptors = self.service.get_interuptors()
        return jsonify(interuptors)
    
    def update_interuptor(self, interuptor_id, request):
        return self.service.update_interuptor(interuptor_id, request)

