from services.generatedCameraService import GeneratedCameraService
from flask import jsonify

class GeneratedCameraController:
    def __init__(self):
        self.service = GeneratedCameraService()

    def get_imageGeneratedCam(self):
        imgGeneratedCam = self.service.get_imageGeneratedCam()
        return jsonify(imgGeneratedCam)
    
    def update_imageGeneratedCam(self, imageGeneratedCam_id, request):
        return self.service.update_imageGeneratedCam(imageGeneratedCam_id, request)


