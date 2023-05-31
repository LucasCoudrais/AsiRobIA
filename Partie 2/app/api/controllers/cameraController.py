from services.cameraService import CameraService
from flask import jsonify

class CameraController:
    def __init__(self):
        self.service = CameraService()

    def get_imageCam(self):
        tempSensors = self.service.get_imageCam()
        return jsonify(tempSensors)
    
    def update_imageCam(self, imageCam_id, request):
        return self.service.update_imageCam(imageCam_id, request)


