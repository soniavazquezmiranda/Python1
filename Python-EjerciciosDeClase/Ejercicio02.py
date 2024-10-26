# SEGUNDO EJERCICIO

'''Escribe un programa que pregunte el nombre y después de que el usuario 
lo introduzca muestre por pantalla el nombre en mayúsculas y el número de caracteres que tiene.
Después deberá escribir el nombre tantas veces como letras contiene el nombre en líneas distintas.
'''

nombre = input("escribe tu nombre:")
nombre_mayuscula = nombre.upper()
print(nombre_mayuscula)

caracter = len(nombre)
print (f"El nombre {nombre} tiene {caracter} caracteres")

for i in range (caracter):
    print(nombre)

    