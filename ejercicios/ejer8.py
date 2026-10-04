import subprocess, sys, time

envio_cocina = subprocess.Popen(
        [sys.executable, "cocina/cocina_lenta.py"],
        text=True,
        )

time.sleep(1)
input("Pulse enter para cancelar el pedido")
print("Cancelando pedido.")

envio_cocina.terminate()
envio_cocina.wait()
print("Pedido finalizado.")