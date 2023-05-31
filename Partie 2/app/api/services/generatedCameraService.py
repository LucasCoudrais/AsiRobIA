from repositories.genericRepository import GenericRepository
from flask import jsonify

class GeneratedCameraService:
    def __init__(self):
        self.repository = GenericRepository('data/generatedCamera.json')

    def get_imageGeneratedCam(self):
        return self.repository.read_entity()
    
    def update_imageGeneratedCam(self, imageGeneratedCam_id, request):
        updated_imageGeneratedCam = request.get_json()
        imageGeneratedCams = self.repository.read_entity()

        for imageGeneratedCam in imageGeneratedCams:
            if imageGeneratedCam['id'] == imageGeneratedCam_id:
                imageGeneratedCam.update(updated_imageGeneratedCam)
                self.repository.write_entity(imageGeneratedCams)
                return jsonify(imageGeneratedCam), 200
        
        return jsonify({'message': 'Image générée camera non trouvé'}), 404


