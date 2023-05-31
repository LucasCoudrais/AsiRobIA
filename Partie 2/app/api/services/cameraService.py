from repositories.genericRepository import GenericRepository
from flask import jsonify

class CameraService:
    def __init__(self):
        self.repository = GenericRepository('data/camera.json')

    def get_imageCam(self):
        return self.repository.read_entity()
    
    def update_imageCam(self, imageCam_id, request):
        updated_imageCam = request.get_json()
        imageCams = self.repository.read_entity()

        for imageCam in imageCams:
            if imageCam['id'] == imageCam_id:
                imageCam.update(updated_imageCam)
                self.repository.write_entity(imageCams)
                return jsonify(imageCam), 200
        
        return jsonify({'message': 'Image camera non trouvé'}), 404


