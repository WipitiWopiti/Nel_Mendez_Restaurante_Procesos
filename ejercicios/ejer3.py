import os, subprocess, time

envio_cocina = subprocess.run(
    ["python", "cocina/cocina.py"],
    capture_output=True,
    text=True)

print(f'''===== INFORME DEL PEDIDO ======
Mensaje de cocina:
{envio_cocina.stdout}
Errores:
{envio_cocina.stderr}
Codigo de retorno:
{envio_cocina.returncode}''')
