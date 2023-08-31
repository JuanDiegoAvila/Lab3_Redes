import ast

class Router:
    def __init__(self, name, neighbors, total_vecinos):
        self.name = name
        self.todos_vecinos = total_vecinos
        self.neighbors = neighbors

        self.diccionario_principal = {
            nombre: [[vecino, self.neighbors.get(vecino, 0)] for vecino in self.todos_vecinos]
        }

        self.getCamino()

    def getCamino(self):
        self.camino = {}
        for nodo in self.diccionario_principal:
            for vecino in self.diccionario_principal[nodo]:
                if vecino[0] != nodo and vecino[0] not in self.neighbors.keys():
                    self.camino[vecino[0]] = ""
                    

    def actualizar_ruta(self, diccionario_vecino):
        nodo1 = self.name
        nodo2 = list(diccionario_vecino.keys())[0]  # Suponemos que diccionario_vecino solo tiene una entrada

        # Obtener la distancia de nodo1 a nodo2
        distancia_nodo1_a_nodo2 = next((v[1] for v in self.diccionario_principal[nodo1] if v[0] == nodo2), 0)

        # Si no hay conexión, entonces no actualizamos
        if distancia_nodo1_a_nodo2 == 0:
            print("No hubo cambios en las rutas")
            return

        actualizados = False

        for vecino in diccionario_vecino[nodo2]:
            nombre_vecino, distancia_nodo2_a_vecino = vecino

            # Si el vecino es el mismo nodo o no hay conexión directa con el vecino, continuamos sin hacer nada
            if nombre_vecino == nodo1 or distancia_nodo2_a_vecino == 0:
                continue

            distancia_total = distancia_nodo1_a_nodo2 + distancia_nodo2_a_vecino

            # Obtener la distancia actual desde nodo1 al nombre_vecino
            distancia_actual_a_vecino = next((v[1] for v in self.diccionario_principal[nodo1] if v[0] == nombre_vecino), 0)

            # Si la distancia total es menor a la distancia actual registrada, o si no hay una ruta existente (distancia 0), actualizamos
            if (distancia_actual_a_vecino == 0) or (distancia_total < distancia_actual_a_vecino):
                for v in self.diccionario_principal[nodo1]:
                    if v[0] == nombre_vecino:
                        v[1] = distancia_total
                        actualizados = True
                        self.camino[nombre_vecino] = nodo2
                        break
                else:
                    # Si el nodo vecino no estaba en el diccionario del nodo1, lo añadimos
                    self.diccionario_principal[nodo1].append([nombre_vecino, distancia_total])
                    actualizados = True
                    self.camino[nombre_vecino] = nodo2

        if not actualizados:
            print("No hubo cambios en las rutas")






    def imprimir_tabla(self):
        print(self.camino)

        print("=" * 30)

        print(f'Nombre: {self.name}')
        print('Vecino | Valor')
        print('----------------')
        
        for vecino, valor in self.diccionario_principal[self.name]:
            print(f'{vecino:^7} | {valor:^5}')

        print(self.diccionario_principal)

        print("=" * 30)

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


nombre = input("Ingrese el nombre del nodo: ")
total_vecinos = input("Ingrese todos los nodos de la topología: ")
vecinos = {}

finished = False
while not finished:
    vecino_nombre = input("Ingrese el nombre del vecino: ")
    vecino_distancia = int(input("Ingrese la distancia de dicho vecino: "))
    vecinos[vecino_nombre] = vecino_distancia
    continuar = input("Desea ingresar otro vecino [si/no]: ")
    
    if continuar == "no":
        finished = True

router = Router(nombre, vecinos, total_vecinos)

opcion = 0

while opcion != 5:
    print("1. Enviar mensaje")
    print("2. Recibir mensaje")
    print("3. Ver tabla de ruteo")
    print("4. Actualizar tabla de ruteo")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        
        receptor = input("Ingrese el nombre del receptor: ")
        mensaje = input("Ingrese el mensaje: ")
        tipo = input("Ingrese el tipo de mensaje: ")
        saltos = int(input("Ingrese la cantidad de saltos: "))

        if tipo == "message":
            pass
        elif tipo == "info":
            cantidad_nodes = int(input("Ingrese la cantidad de nodos: "))
            

        
    elif opcion == 2:

        emisor = input("Ingrese el nombre del emisor: ")
        receptor = input("Ingrese el nombre del receptor: ")
        mensaje = input("Ingrese el mensaje: ")
        tipo = input("Ingrese el tipo de mensaje: ")
        intermediarios = input("Ingrese los intermediarios: ")
        intermediarios = intermediarios.split(",")
        saltos = int(input("Ingrese la cantidad de saltos: "))
    
    elif opcion == 3:
        router.imprimir_tabla()

    elif opcion == 4:
        vecino_nombre = input("Ingrese el nombre del nodo de la tabla: ")
        vecino_distancia = ast.literal_eval(input("Ingrese la tabla de dicho nodo: "))

        print(vecino_distancia)
        router.actualizar_ruta(vecino_distancia)



    elif opcion == 5:
        break
