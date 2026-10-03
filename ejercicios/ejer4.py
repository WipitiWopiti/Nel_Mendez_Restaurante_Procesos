import os, subprocess, time

envio_cocina = subprocess.run(
    ["python", "cocina/cocina_error.py"],
    capture_output=True,
    text=True)

print(f'''===== EJECUCION ERRONEA 1 ======
Mensaje de cocina:
{envio_cocina.stdout}
Errores:
{envio_cocina.stderr}
Codigo de retorno:
{envio_cocina.returncode}''')


print(f'''===== EJECUCION ERRONEA 2 ======''')
try:
    envio_cocina = subprocess.run(
        ["python", "cocina/cocina_error.py"],
        capture_output=True,
        check=True,
        text=True)
    
except subprocess.CalledProcessError:
    print(f'''ERROR: El pedido no ha podido prepararse''')