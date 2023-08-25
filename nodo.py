class Nodo(object):
    def __init__(self, nombre, vecinos):
        self.nombre = nombre
        self.vecinos = vecinos
        self.mensajes = []
    
    def addVecino(self, vecino):
        self.vecinos.append(vecino)
    
    def paquete(self, type, headers, payload):

        paquete = {
            "type": type,
            "headers": headers,
            "payload": payload
        }

        if paquete not in self.mensajes:
            self.mensajes.append(paquete)
            return paquete
    
    def __repr__(self):
        return "Nodo: " + str(self.nombre) + "Vecinos: " + str(self.vecinos)