import subprocess, sys



    
pedido = input("Introduzca el pedido que desea: ")

envio_cocina = subprocess.Popen(
        [sys.executable, "cocina/cocina_pedido.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

print(f"Sistema envía: {pedido}")

salida, errores = envio_cocina.communicate(input=pedido)

if errores:
    print("Errores: ", errores)

print(salida)