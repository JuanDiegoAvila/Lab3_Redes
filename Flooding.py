from nodo import *

class Flooding(object):
    def __init__(self):
        pass

    def enviar_mensaje(self, tipo, saltos, origen, mensaje, destino, intermediario, intermediarios = []):
        temp = ""
        bandera = False

        if type(origen).__name__ == "Nodo":
            temp = origen.nombre
        
        else:
            temp = origen
            origen = intermediario
            bandera = True

        if origen.nombre not in intermediarios:
            intermediarios.append(origen.nombre)


        if temp == destino:
            return mensaje
        
        else:

            for vecino in origen.vecinos:

                if vecino in intermediarios:
                    continue
                
                if bandera:
                    if vecino != temp:
                        print("\n Enviar este paquete a :", vecino)
                        print()
                        
                        paquete = {
                            "type": tipo, 
                            "headers": {
                                "from": temp, 
                                "to": destino,
                                "hop_count": saltos,
                                "intermediarios": ",".join(intermediarios)
                            }, 
                            "payload": mensaje
                        }

                        print(paquete)
                        
                    else:
                        pass
                else:

                    if vecino != origen.nombre:
                        print("\n Enviar este paquete a :", vecino)
                        print()
                        
                        paquete = {
                            "type": tipo, 
                            "headers": {
                                "from": temp, 
                                "to": destino,
                                "hop_count": saltos,
                                "intermediarios": ",".join(intermediarios)
                            }, 
                            "payload": mensaje
                        }

                        print(paquete)
                    else:
                        pass

    def recibir_mensaje(self, actual, receptor, mensaje, tipo, saltos, emisor, intermediarios):
        if saltos > 0 and receptor != actual.nombre:

            intermediarios.append(actual.nombre)
            saltos -= 1
            for vecino in actual.vecinos:

                if vecino not in intermediarios:
                    self.enviar_mensaje(tipo, saltos, emisor, mensaje, receptor, actual, intermediarios)
                    print()
        else:
            print("\nMensaje recibido")
            print(mensaje)


nombre = input("Ingrese el nombre del nodo: ")
finished = False
vecinos = {}

while not finished:
    vecino_nombre = input("Ingrese el nombre del vecino: ")
    vecino_distancia = input("Ingrese la distancia de dicho vecino: ")
    vecinos[vecino_nombre] = vecino_distancia
    continuar = input("Desea ingresar otro vecino [si/no]: ")

    if continuar == "no":
        finished = True

node = Nodo(nombre, vecinos)

opcion = 0
Flooding = Flooding()

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
            Flooding.enviar_mensaje(tipo, saltos, node, mensaje, receptor, node)
        
    elif opcion == 2:

        emisor = input("Ingrese el nombre del emisor: ")
        receptor = input("Ingrese el nombre del receptor: ")
        mensaje = input("Ingrese el mensaje: ")
        tipo = input("Ingrese el tipo de mensaje: ")
        intermediarios = input("Ingrese los intermediarios: ")
        intermediarios = intermediarios.split(",")
        saltos = int(input("Ingrese la cantidad de saltos: "))

        if tipo == "message":
            Flooding.recibir_mensaje(node, receptor, mensaje, tipo, saltos, emisor, intermediarios)

    elif opcion == 3:
        break
        
    

