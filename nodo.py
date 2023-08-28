class Nodo(object):
    def __init__(self, nombre, vecinos = None):
        self.nombre = nombre
        self.vecinos = [] if vecinos is None else vecinos
        self.distancias = {}
        self.mensajes = []
    
    def addVecino(self, vecino, distancia = 0):
        self.vecinos.append(vecino)
        self.distancias[vecino.nombre] = distancia
        vecino.distancias[self.nombre] = distancia
    
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
        vecinos_nombres = [vecino.nombre for vecino in self.vecinos]
        return " Nodo: " + str(self.nombre) + " Vecinos: " + str(vecinos_nombres) + " Distancias: " + str(self.distancias)