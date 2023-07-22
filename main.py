# python3 -m flask --app main run --host=0.0.0.0
from flask import Flask, request
from flask_cors import CORS, cross_origin
from ECUSimulator.supported import assetto_corsa
import logging
import socket

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

assettoCorsa = assetto_corsa.AssettoCorsa()
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
	file = open('./src/ECUs/ft550.html',mode='r')
	return file.read()


