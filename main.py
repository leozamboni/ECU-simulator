# python3 -m flask --app main run --host=0.0.0.0
from flask import Flask, request
from flask_cors import CORS, cross_origin
from compatible import assetto_corsa
import socket

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

assettoCorsa = assetto_corsa.AssettoCorsa()
localNetAddr = s.getsockname()[0]
s.close()

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
	file = open('./ECUs/ft550.html',mode='r')
	return file.read()


print(f'Access http://{localNetAddr}:5000/ecu on your mobile')