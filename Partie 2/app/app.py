from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    message = {'message': 'Bienvenue !'}
    return jsonify(message)

@app.route('/sensors', methods=['GET'])
def get_sensors():
    sensors = read_sensors()
    return jsonify(sensors)

@app.route('/sensors/<int:sensor_id>', methods=['PUT'])
def update_sensor(sensor_id):
    updated_sensor = request.get_json()
    sensors = read_sensors()

    for sensor in sensors:
        if sensor['id'] == sensor_id:
            sensor.update(updated_sensor)
            write_sensors(sensors)
            return jsonify(sensor), 200
    
    return jsonify({'message': 'Capteur non trouvé'}), 404

@app.route('/proximitySensors', methods=['GET'])
def get_proximitySensors():
    proximitySensors = read_proximitySensors()
    return jsonify(proximitySensors)


@app.route('/proximitySensors/<int:proximitySensor_id>', methods=['PUT'])
def update_proximitySensors(proximitySensor_id):
    print("TEST")
    updated_proximitySensor = request.get_json()
    proximitySensors = read_proximitySensors()

    for proximitySensor in proximitySensors:
        if proximitySensor['id'] == proximitySensor_id:
            proximitySensor.update(updated_proximitySensor)
            write_proximitySensors(proximitySensors)
            return jsonify(proximitySensor), 200
    
    return jsonify({'message': 'Capteur de proximité non trouvé'}), 404



def read_sensors():
    with open('data/sensors.json', 'r') as file:
        sensors = json.load(file)
    return sensors

def write_sensors(sensors):
    with open('data/sensors.json', 'w') as file:
        json.dump(sensors, file)
        
def read_proximitySensors():
    with open('data/proximitySensors.json', 'r') as file:
        proximitySensors = json.load(file)
    return proximitySensors

def write_proximitySensors(proximitySensors):
    with open('data/proximitySensors.json', 'w') as file:
        json.dump(proximitySensors, file)

if __name__ == '__main__':
    app.run()
