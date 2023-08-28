import ast

class Router:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors
        self.routing_table = {name: (0 if name == self.name else float('inf'), self.name) for name in neighbors}
    
    def update_routing_table(self, neighbor_name, neighbor_routing_table):
        for dest, (cost, source) in neighbor_routing_table.items():
            if dest in self.routing_table:
                if self.routing_table[dest][0] > cost:
                    self.routing_table[dest] = (cost, neighbor_name)
            else:
                self.routing_table[dest] = (cost, neighbor_name)
    
    def print_routing_table(self):
        print(f"Routing table of {self.name}:")
        for dest, (cost, source) in self.routing_table.items():
            print(f"Destination: {dest}, Cost: {cost}, Source: {source}")
        
        # Print the routing table in dictionary format
        print("Routing table as dictionary:", self.routing_table)

nombre = input("Ingrese el nombre del nodo: ")
vecinos = {}

finished = False
while not finished:
    vecino_nombre = input("Ingrese el nombre del vecino: ")
    vecino_distancia = int(input("Ingrese la distancia de dicho vecino: "))
    vecinos[vecino_nombre] = vecino_distancia
    continuar = input("Desea ingresar otro vecino [si/no]: ")
    if continuar == "no":
        finished = True

router = Router(nombre, vecinos)

opcion = 0

while opcion != 3:
    print("1. Enviar mensaje")
    print("2. Recibir mensaje")
    print("3. Salir")
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
    
    # elif opcion == 3:
    #     router.print_routing_table()

    # elif opcion == 4:
    #     vecino_nombre = input("Ingrese el nombre del nodo de la tabla: ")
    #     vecino_distancia = ast.literal_eval(input("Ingrese la tabla de dicho nodo: "))

    #     print(vecino_distancia)
    #     router.update_routing_table(vecino_nombre, vecino_distancia)



    elif opcion == 5:
        break
