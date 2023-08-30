import ast

class Router:
    def __init__(self, name, neighbors, total_vecinos):
        self.name = name
        self.todos_vecinos = total_vecinos
        self.neighbors = neighbors

        self.diccionario_principal = {
            nombre: [[vecino, self.neighbors.get(vecino, 0)] for vecino in self.todos_vecinos]
        }

    def actualizar_ruta(self, diccionario_vecino):
        nodo1 = self.name
        nodo2 = list(diccionario_vecino.keys())[0]

        distancia_nodo1_a_nodo2 = [v[1] for v in self.diccionario_principal[nodo1] if v[0] == nodo2][0]
        actualizados = False

        for vecino in diccionario_vecino[nodo2]:
            nombre_vecino, distancia_nodo2_a_vecino = vecino
            if nombre_vecino != nodo1:  # No queremos comparar el nodo original con sí mismo

                distancia_total = distancia_nodo1_a_nodo2 + distancia_nodo2_a_vecino
                
                vecinos_actuales = {v[0]: v[1] for v in self.diccionario_principal[nodo1]}
                
                # Si el vecino no está en el diccionario original o si la nueva distancia es menor
                if distancia_total < vecinos_actuales[nombre_vecino] or vecinos_actuales[nombre_vecino] == 0:
                    if nombre_vecino in vecinos_actuales:
                        # Encuentra y actualiza la distancia en el diccionario
                        for v in self.diccionario_principal[nodo1]:
                            if v[0] == nombre_vecino:
                                actualizados = True
                                v[1] = distancia_total
        
        if not actualizados:
            print("Ya no se pueden actualizar las rutas")

    def imprimir_tabla(self):

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

print(vecinos)

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
