import subprocess, sys, os, time

plato = input()
tiempo = input()

print(f'''
Plato: {plato}
PID: {os.getpid()}''')

time.sleep(int(tiempo))