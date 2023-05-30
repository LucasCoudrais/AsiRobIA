from flask import Flask, request, jsonify
from controllers.tempController import TempController
from controllers.proximityController import ProximityController

app = Flask(__name__)

temp_controller = TempController()
proximity_controller = ProximityController()

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

if __name__ == '__main__':
    app.run(debug=True)