import requests
import json
from zeroconf import Zeroconf
class GestorCalefaccio:

    engegada = bool(False)
    calefaccio = str("")

    def __init__(self):
        name="calefaccio.local."
        type="_http._tcp.local."
        zeroconf = Zeroconf()    
        info = zeroconf.get_service_info(type, name)              
        if info:
            self.calefaccio = info.parsed_addresses()[0]
        zeroconf.close()
    
    def test(self):
        try:
            if len(self.calefaccio) > 0:
                response = requests.get("https://%s/test" % self.calefaccio, verify = False)    
                return response.json()
            else:
                return json.dumps("KO")
        except:
            return json.dumps("KO")
            
    def activar(self):
        try:
            response = requests.get("https://%s/activar" % self.calefaccio, verify = False)
            self.engegada= True
            return response.json()
        except:
            return json.dumps("KO")

    def desactivar(self):
        try:
            response = requests.get("https://%s/desactivar" % self.calefaccio, verify = False)
            self.engegada = False
            return response.json()
        except:
            return json.dumps("KO")

    def retornarTemperatura(self):
        try:
            response = requests.get("https://%s/temperatura" % self.calefaccio, verify = False)
            return response.json()
        except:
            return json.dumps("KO")

    def estaEngegada(self):
        return json.dumps(self.engegada)