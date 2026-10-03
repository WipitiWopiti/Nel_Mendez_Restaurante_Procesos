import subprocess, sys

pedido_hamburguesa = subprocess.Popen(
    [sys.executable, "cocina/hamburguesa.py"],
    text=True
)

pedido_pizza = subprocess.Popen(
    [sys.executable, "cocina/pizza.py"],
    text=True
)

pedido_postre = subprocess.Popen(
    [sys.executable, "cocina/postre.py"],
    text=True
)

pedido_hamburguesa.wait()
pedido_pizza.wait()
pedido_postre.wait()