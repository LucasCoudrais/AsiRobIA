from flask import Flask, Response, render_template
import cv2
from PIL import Image
import numpy as np

app = Flask(__name__)

def detect_objects(frame):
    # Code pour détecter les objets sur l'image (utilisez votre propre code de détection)
    # Remplacez cette fonction par votre propre logique de détection d'objets
    # Cette fonction doit prendre une image (sous forme de tableau numpy) en entrée et retourner l'image avec les détections

    # Par exemple, utilisons un simple dessin de rectangle autour d'une détection fictive
    height, width, _ = frame.shape
    start_point = (int(width * 0.25), int(height * 0.25))
    end_point = (int(width * 0.75), int(height * 0.75))
    color = (0, 255, 0)  # Vert
    thickness = 2
    cv2.rectangle(frame, start_point, end_point, color, thickness)

    return frame

def generate_frames():
    video_path = "../video.mp4"  # Spécifiez le lien vers votre flux MJPEG

    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir le format d'image BGR en RGB
        frame = detect_objects(frame)  # Appliquer les détections sur l'image

        img_pil = Image.fromarray(frame)
        img_pil.thumbnail((640, 480))  # Redimensionner l'image si nécessaire

        frame = np.array(img_pil)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route('/video_feed_filtered')
def video_feed_filtered():
    return Response(generate_frames_filtered(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)