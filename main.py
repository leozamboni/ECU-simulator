# python3 -m flask --app main run --host=0.0.0.0
from flask import Flask, request
from flask_cors import CORS, cross_origin
from compatible import assetto_corsa

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

AssettoCorsa = assetto_corsa.AssettoCorsa()

@app.route("/")
@cross_origin()
def get_values():
    return {
		"physics":AssettoCorsa.read_physics(),
		"static": AssettoCorsa.read_static(),
	}

@app.route("/ecu")
@cross_origin()
def index():
	file = open('./ECUs/ft550.html',mode='r')
	return file.read()
