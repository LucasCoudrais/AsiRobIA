from flask import Flask, Response, render_template
import cv2
from PIL import Image
import numpy as np

app = Flask(__name__)
        
def generate_frames_filtered():
    video_path = "../video.mp4"  # Spécifiez le lien vers votre flux MJPEG

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
        
def generate_frames_detect_face():
    video_path = "../people.mp4"  # Spécifiez le lien vers votre flux MJPEG

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed_filtered')
def video_feed_filtered():
    return Response(generate_frames_filtered(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route('/video_feed_detect_face')
def video_feed_detect_face():
    return Response(generate_frames_detect_face(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)