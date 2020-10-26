import flask
import requests
import json
from zeroconf import Zeroconf
from GestorCalefaccio import GestorCalefaccio

app = flask.Flask(__name__)
gc = GestorCalefaccio()
app.config["DEBUG"] = False

@app.route('/', methods=['GET'])
def index():
    return("I'm alive")

@app.route('/test', methods=['GET'])
def test():    
    return gc.test()
    
@app.route('/activar', methods=['GET'])
def activar():    
    return gc.activar()

@app.route('/desactivar', methods=['GET'])
def desactivar():
    return gc.desactivar()

@app.route('/temperatura', methods=['GET'])
def retornarTemperatura():
    return gc.retornarTemperatura()

@app.route('/engegada', methods=['GET'])
def estaEngegada():
    return gc.estaEngegada()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
