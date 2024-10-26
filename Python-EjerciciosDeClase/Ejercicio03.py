# TERCER EJERCICIO

'''Escribe los números pares del 2 hasta un número que se pida por teclado previamente.
'''

numero_maximo = int (input("escribe un numero maximo:"))

if numero_maximo >=2:
    for numero in range (numero_maximo):
        if numero %2 == 0:
             print(numero + 2)
