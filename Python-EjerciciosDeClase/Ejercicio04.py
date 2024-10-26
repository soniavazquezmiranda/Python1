# CUARTO EJERCICIO

''' Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable,
 y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> 
 es el índice de masa corporal calculado redondeado con dos decimales.
Para calcular IMC se divide el peso, en kilos, por la altura, en metros al cuadrado.
'''
peso = int (input( "Escriba su peso en kg: "))
altura = float (input("Escribe su altura en cm: "))

imc = round (peso/ (altura/100)** 2,2)

print(f"Tu indice de masa corporal es {imc}")

