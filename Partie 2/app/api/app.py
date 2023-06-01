from flask import Flask, request, Response, render_template
import cv2
from PIL import Image
import numpy as np

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

@app.route('/')
def index():
    return render_template('index.html')



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



@app.route('/video_feed_filtered')
def video_feed_filtered():
    return Response(generate_frames_filtered(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_detect_face')
def video_feed_detect_face():
    return Response(generate_frames_detect_face(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')





def generate_frames_detect_face():
    video_path = "people.mp4"  # Spécifiez le lien vers votre flux MJPEG

    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir le format d'image BGR en RGB
        
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Convertir l'image en niveaux de gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Détecter les visages dans l'image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Dessiner un rectangle autour de chaque visage détecté
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        img_pil = Image.fromarray(frame)
        img_pil.thumbnail((640, 480))  # Redimensionner l'image si nécessaire

        frame = np.array(img_pil)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def generate_frames_filtered():
    video_path = "video.mp4"  # Spécifiez le lien vers votre flux MJPEG

    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir le format d'image BGR en RGB
        
        frame = cv2.Canny(frame, 30, 150)
        
        img_pil = Image.fromarray(frame)
        img_pil.thumbnail((640, 480))  # Redimensionner l'image si nécessaire

        frame = np.array(img_pil)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

if __name__ == '__main__':
    app.run(debug=True)