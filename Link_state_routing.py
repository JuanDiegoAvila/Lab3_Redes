from nodo import *
import heapq

class LinkStateRouting():
    def __init__(self):
        self.topologia = {}
    
    def enviar_topologia(self, nodo):
        return nodo.distancias  # Cambio aquí

    def recibir_topologia(self, nodo, mensaje):
        self.topologia[nodo.nombre].distancias = mensaje  # Cambio aquí

    def agregar_nodo(self, nodo):
        self.topologia[nodo.nombre] = nodo

    def calcular_info(self, nodo):
        for key in nodo.distancias:  # Cambio aquí
            print(key)

    def calcular_ruta(self, origen, destino):
        distancias = {nodo: float('inf') for nodo in self.topologia}
        predecesores = {nodo: None for nodo in self.topologia}  # Diccionario de predecesores
        distancias[origen] = 0
        nodos_pendientes = [(0, origen)]
        visitados = set()

        while nodos_pendientes:
            distancia_actual, nodo_actual = heapq.heappop(nodos_pendientes)
            if nodo_actual in visitados:
                continue
            visitados.add(nodo_actual)

            for vecino, distancia in self.topologia[nodo_actual].distancias.items():
                nueva_distancia = distancia_actual + distancia
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = nodo_actual  # Actualizar el predecesor para este vecino
                    heapq.heappush(nodos_pendientes, (nueva_distancia, vecino))

        # Reconstruir el camino desde el destino al origen usando el diccionario de predecesores
        camino = []
        nodo_actual = destino
        while nodo_actual is not None:
            camino.insert(0, nodo_actual)  # Agregar al inicio para reconstruir en el orden correcto
            nodo_actual = predecesores[nodo_actual]

        return camino
    
    def ver_topologia(self):
        for nodo, detalles in self.topologia.items():
            print(f"{nodo}: {detalles.distancias}")  # Cambio aquí

    def enviar_mensaje(self, tipo, saltos, origen, mensaje, destino, intermediario):
        
        origen_ = None
        if type(origen).__name__ == "Nodo":
            origen_ = origen.nombre
        else:
            origen_ = origen
            origen = intermediario.nombre

        

        camino = self.calcular_ruta(origen, destino)
        next = camino[1]

        print("\n Enviar este paquete a :", next)

        paquete = {
            "type": tipo, 
            "headers": {
                "from": origen_, 
                "to": destino,
                "hop_count": saltos
            }, 
            "payload": mensaje
        }

        print(paquete)

    def recibir_mensaje(self, emisor, receptor, mensaje, tipo, saltos, actual):
        if receptor == actual.nombre:
            print("Mensaje recibido: ", mensaje)
            return
    
        if saltos == 0:
            print("Mensaje perdido")
            return
        
        saltos -= 1
        self.enviar_mensaje(tipo, saltos, emisor, mensaje, receptor, actual)

lsr = LinkStateRouting()

nombre = input("Ingrese el nombre del nodo: ")
resto = input("Ingrese el nombre del resto de nodos (X,Y,Z...) : ")
resto = resto.split(",")

lNodos = []
lNodos.append(nombre)
lNodos.extend(resto)

actual = None

nodos = []
vecinos = {}
for nodo in lNodos:
    vecinos[nodo] = {}
    nodo_temp = Nodo(nodo)
    nodos.append(nodo_temp)
    print()

    if nodo == nombre:
        actual = nodo_temp

    for nodo2 in lNodos:
        if nodo != nodo2:
            if nodo2 not in vecinos.keys() or nodo not in vecinos[nodo2]: 
                distancia = int(input(f"Ingrese la distancia entre {nodo} y {nodo2}: "))
                if distancia > 0:
                    vecinos[nodo][nodo2] = distancia

for nodo_obj in nodos:
    nombre_nodo = nodo_obj.nombre
    for vecino_nombre, distancia in vecinos[nombre_nodo].items():
        for vecino_obj in nodos:
            if vecino_obj.nombre == vecino_nombre:
                nodo_obj.addVecino(vecino_obj, distancia)
                break
        
for nodo in nodos:
    lsr.agregar_nodo(nodo)


for nodo in nodos:
    mensaje = lsr.enviar_topologia(nodo)
    lsr.recibir_topologia(nodo, mensaje)


print("\nTopologia de la red")
lsr.ver_topologia()
print()

opcion = 0
while opcion != 3:
    print("1. Enviar mensaje")
    print("2. Recibir mensaje")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    print()
    if opcion == 1:
        
        receptor = input("Ingrese el nombre del receptor: ")
        mensaje = input("Ingrese el mensaje: ")
        tipo = input("Ingrese el tipo de mensaje: ")
        saltos = int(input("Ingrese la cantidad de saltos: "))

        if tipo == "message":
            lsr.enviar_mensaje(tipo, saltos, actual.nombre, mensaje, receptor, actual)

        
    elif opcion == 2:

        emisor = input("Ingrese el nombre del emisor: ")
        receptor = input("Ingrese el nombre del receptor: ")
        mensaje = input("Ingrese el mensaje: ")
        tipo = input("Ingrese el tipo de mensaje: ")
        saltos = int(input("Ingrese la cantidad de saltos: "))

        if tipo == "message":
            lsr.recibir_mensaje(emisor, receptor, mensaje, tipo, saltos, actual)


    elif opcion == 3:
        break