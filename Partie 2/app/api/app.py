from flask import Flask, request, jsonify, Response
from controllers.tempController import TempController
from controllers.proximityController import ProximityController
from controllers.interuptorController import InteruptorController
from controllers.cameraController import CameraController
from controllers.generatedCameraController import GeneratedCameraController

app = Flask(__name__)

temp_controller = TempController()
proximity_controller = ProximityController()
interuptor_controller = InteruptorController()
camera_controller = CameraController()
generatedCamera_controller = GeneratedCameraController()

@app.route('/', methods=['GET'])
def hello():
    message = {'message': 'Bienvenue !'}
    return jsonify(message)



@app.route('/tempSensors', methods=['GET'])
def get_tempSensors():
    return temp_controller.get_tempSensors()

@app.route('/tempSensor/<int:tempSensor_id>', methods=['PUT'])
def update_tempSensor(tempSensor_id):
    return temp_controller.update_tempSensor(tempSensor_id, request)



@app.route('/proximitySensors', methods=['GET'])
def get_proximitySensors():
    return proximity_controller.get_proximitySensors()

@app.route('/proximitySensor/<int:proximitySensors_id>', methods=['PUT'])
def update_proximitySensor(proximitySensors_id):
    return proximity_controller.update_proximitySensor(proximitySensors_id, request)



@app.route('/interuptors', methods=['GET'])
def get_interuptors():
    return interuptor_controller.get_interuptors()

@app.route('/interuptor/<int:interuptor_id>', methods=['PUT'])
def update_interuptor(interuptor_id):
    return interuptor_controller.update_interuptor(interuptor_id, request)



@app.route('/streamCamera', methods=['GET'])
def stream_camera():
    video_path = 'video.mp4'  # Chemin vers votre fichier vidéo

    def generate():
        with open(video_path, 'rb') as video_file:
            while True:
                video_data = video_file.read(1024)
                if not video_data:
                    break
                yield video_data

    return Response(generate(), mimetype='video/mp4')



@app.route('/imageCameras', methods=['GET'])
def get_imageCam():
    return camera_controller.get_imageCam()

@app.route('/imageCamera/<int:imageCam_id>', methods=['PUT'])
def update_imageCam(imageCam_id):
    return camera_controller.update_imageCam(imageCam_id, request)


@app.route('/imageGeneratedCameras', methods=['GET'])
def get_imageGeneratedCam():
    return generatedCamera_controller.get_imageGeneratedCam()

@app.route('/imageGeneratedCamera/<int:imageGeneratedCam_id>', methods=['PUT'])
def update_imageGeneratedCam(imageGeneratedCam_id):
    return generatedCamera_controller.update_imageGeneratedCam(imageGeneratedCam_id, request)


if __name__ == '__main__':
    app.run(debug=True)