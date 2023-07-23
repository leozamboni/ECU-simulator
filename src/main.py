# python3 -m flask --app main run --host=0.0.0.0
from flask import Flask, request
from flask_cors import CORS, cross_origin
from settings import webTelemetryDisplaySettings
from supported.assetto_corsa.assetto_corsa import AssettoCorsa
import logging
import socket
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

gameDir = webTelemetryDisplaySettings['game'].lower().replace(" ", "_")
displayDir = webTelemetryDisplaySettings['display']

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

assettoCorsa = AssettoCorsa()
localNetAddr = s.getsockname()[0]
s.close()

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

print(f'Access http://{localNetAddr}:5000/ecu on your mobile')

@app.route("/")
@cross_origin()
def get_values():
    return {
		"physics":assettoCorsa.read_physics(),
		"static": assettoCorsa.read_static(),
	}

@app.route("/ecu")
@cross_origin()
def index():
	file = open(f'./src/displays/{gameDir}/{displayDir}/{displayDir}.html',mode='r')
	return file.read()


