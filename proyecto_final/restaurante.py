import subprocess, sys, os, time

def crear_pedido():
    '''Crea un pedido con Popen() y muestra su información'''

    plato = input("Introduzca el plato que desea: ")
    try:
        tiempo = int(input("Introduzca el tiempo de preparación: "))
    except:
        print("Debe introducir un numero entero.")
        return
    
    print(f'''
Nombre del plato: {plato}
Tiempo: {tiempo} \n''')
    
    print("Pedido enviado a cocina")
    envio_cocina = subprocess.Popen(
            [sys.executable, "proyecto_final/cocina_final.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )
    
    # salida, errores = envio_cocina.communicate(input=f'''{plato}\n{tiempo}''')
    # Encontré esto porque resulta que el communicate() espera a que termine todo el hijo antes de mandar la respuesta
    envio_cocina.stdin.write(f'''{plato}\n{tiempo}''')
    envio_cocina.stdin.close()
    global PEDIDOS
    PEDIDOS.append((envio_cocina, plato))
    return
    
def consultar_cocina():
    ''''Muestra todos los pedidos conocidos y su estado'''
    
    print("===== ESTADO COCINA =====")
    for pedido in PEDIDOS:
        if pedido[0].poll() is None:
            print(f'''PID {pedido[0].pid} | {pedido[1]} | PREPARANDO''')
        else:
            print(f'''PID {pedido[0].pid} | {pedido[1]} | TERMINADO''')
    
    return

def cancelar_preparacion():
    '''Cancela un pedido a partir del PID'''

    try:
        pid_buscar = int(input("Introduzca el PID del pedido que desee terminar: "))
    except:
        print("El PID debe ser un numero")
        return
    
    for pedido in PEDIDOS:
        if pedido[0].pid == pid_buscar:
            print("Pedido encontrado")
            if pedido[0].poll() is None:
                pedido[0].terminate()
                pedido[0].wait()
                print("El pedido ha sido finalizado correctamente")
            else:
                print("El pedido ya estaba finalizado")
            return
        
    print("Pedido no encontrado")
    return
    
def listar_pedidos_terminados():
    '''Muestra los pedidos terminados'''


if __name__ == "__main__":
    
    PEDIDOS = []
    
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
                crear_pedido()
            case 2:
                consultar_cocina()
            case 3:
                cancelar_preparacion()
            case 4:
                listar_pedidos_terminados()
            case 5:
                print("Adios")
                exit()
            case _:
                print("Debe introducir un numero dentro de las opciones.")
                continue