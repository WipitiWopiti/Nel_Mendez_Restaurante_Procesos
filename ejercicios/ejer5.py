import subprocess


try:
    envio_cocina = subprocess.run(
        ["python", "cocina/cocina_lenta.py"],
        capture_output=True,
        text=True,
        timeout=5)

except subprocess.TimeoutExpired:
    print(f"ERROR: el tiempo maximo de preparacion ha sido superado")
    print("Pedido cancelado")
    
