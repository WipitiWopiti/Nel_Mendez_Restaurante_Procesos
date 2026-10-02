import os, subprocess, time


print("Pedido recibido")
print("Enviando pedido a cocina...")
envio_cocina = subprocess.run(["python", "cocina/cocina.py"])
print("Pedido finalizado")