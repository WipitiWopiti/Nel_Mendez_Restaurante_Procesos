# Nel_Mendez_Restaurante_Procesos

Hay gente que hace esto super bonito pero voy a tener que dejar eso para otro momento

# Descripcion

Esta practica implementa un sistema de comunicacion entre la sala y la cocina de un restaurante simulando tareas como procesos independientes en Python. A través de varios ejercicios progresivos y un proyecto final.

# Requisitos

Para ejecutar y probar esta práctica no se requiere la instalación de dependencias externas ni entornos virtuales, ya que solo se utilizan librerías nativas del lenguaje.

Python: Versión `3.8` o superior
Entorno / Sistema Operativo: Compatible con Linux, macOS y Windows

# Estructura

Nel_Mendez_RestauranteProcesos/
|
+-- README.md
+-- .gitignore
+-- informe/
| +-- Informe.pdf
|
+-- ejercicios/
| +-- ejer1.py
| +-- ejer2.py
| +-- ejer3.py
| +-- ejer4.py
| +-- ejer5.py
| +-- ejer6.py
| +-- ejer7.py
| +-- ejer8.py
| +-- ejer9.py
|
+-- cocina/
| +-- cocina.py
| +-- cocina_error.py
| +-- cocina_lenta.py
| +-- hamburguesa.py
| +-- pizza.py
| +-- postre.py
| +-- cocina_pedido.py
|
+-- proyecto_final/
+-- restaurante.py
+-- cocina_final.py

# Intrucciones para restaurante.py

Restaurante.py como todo el resto de programas deben ejecutarse estando ubicado en el directorio principal del proyecto debido al uso de rutas relativas en su desarrollo

# Conceptos de procesos utilizados

# Flujo de ramas empleado

Para garantizar un historial claro y un desarrollo estructurado, se ha aplicado un modelo simplificado de GitFlow:   

main: Contiene la versión estable, comprobada y lista para la entrega final del proyecto (v1.0).   develop: Rama principal de trabajo donde se integran de forma progresiva las diferentes funcionalidades terminadas.   

feature/*: Cada ejercicio o módulo del proyecto se ha desarrollado de manera aislada en su propia rama de características