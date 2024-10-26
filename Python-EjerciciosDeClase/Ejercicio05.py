
# QUINTO EJERCICIO

''' Escribe un programa que genere una multiplicación de dos números del 2 al 10 al azar, 
pregunte por el resultado y 
diga si se ha dado la respuesta correcta  o no es correcta, 
y en este caso escribir la correcta.'''

import random

numero_azar1 = random.randint(2, 10)
numero_azar2 = random.randint(2, 10)

numero = numero_azar1 * numero_azar2
numero_usuario = int (input("Escribe un numero: "))

if numero_usuario == numero:
    print("Felicidades, has acertado!")

else:
    print("Lo siento, no has acertado.")
    print(f"El nuemro seleccionado era {numero}")
