#Fecha: 14 - 10 -21
#Descripción: Programa para verificar si un numero introducido por el
#usuario es par o impar.
#Tecnologias: Python
var = float(input('Ingrese un número: '))
op = var % 2
if op == 0:
    print("Numero Par")
else:
    print("El numero es impar: ")
#OPERADOR TERNARIO
# print("Imprimir esto si es verdadero ") if condicion else print("Condición Falsa")
