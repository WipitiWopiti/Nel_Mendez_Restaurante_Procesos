import subprocess, sys, time

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


estado_hamburguesa = "PREPARANDO"
estado_pizza = "PREPARANDO"
estado_postre = "PREPARANDO"

while True:
    
    if pedido_hamburguesa.poll() != None:
        estado_hamburguesa = "TERMINADO"
    if pedido_pizza.poll() != None:
        estado_pizza = "TERMINADO"
    if pedido_postre.poll() != None:
        estado_postre = "TERMINADO"
    
    print(f'''===== ESTADO DE COCINA =====
Hamburguesa: {estado_hamburguesa}
Pizza: {estado_pizza}
Postre: {estado_postre} \n''')
    
    if pedido_hamburguesa.poll() != None and pedido_pizza.poll() != None and pedido_postre.poll() != None:
        break
    
    time.sleep(1)