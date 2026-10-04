import subprocess, sys, os, time

def crear_pedido():
    '''Crea un pedido con Popen() y muestra su información'''

def consultar_cocina():
    ''''Muestra todos los pedidos conocidos y su estado'''

def cancelar_preparacion():
    '''Cancela un pedido a partir del PID'''

def listar_pedidos_terminados():
    '''Muestra los pedidos terminados'''


if __name__ == "__main__":
    
    while True:
        time.sleep(1)
        print(f'''
===================================
RESTAURANTE PSP
===================================\n
1. Crear pedido \n
2. Consultar cocina \n
3. Cancelar preparación \n
4. Ver pedidos terminados \n
5. Salir \n''')
        
        try:
            inp = int(input("Seleccione una opción: "))
        except:
            print("Debe introducir un numero")
            continue

        match inp:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                print("Adios")
                exit()
            case _:
                print("Debe introducir un numero dentro de las opciones.")
                continue