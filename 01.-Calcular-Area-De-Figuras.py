#Fecha Inicio: 12-10-21
#Fecha Fin: 13-10-21
#Tema: Ejercicio para calcular el area de distintas figuras.
#Tecnologias:Python 3
import math

def areaTriangulo():
    base = float(input('Ingrese Base: '))
    altura = float(input('Ingrese Altura: '))

    return (base * altura) / 2

def areaCuadrado():
    lado1 = float(input('Ingrese lado 1:'))
    lado2 = float(input('Ingrese lado 2: '))

    return lado1 * lado2

def areaRetangulo():
    altura = float(input('Ingresa la altura: '))
    base = float(input('Ingresa la base: '))

    return altura * base

def areaHexagono():
    lado = float(input('Ingresa longitud de uno de los lados: '))
    #Calculando el perimetro
    perimetro = lado * 6
    #Calcular Apotema
    apotema = math.sqrt(lado**2 - (lado/2)**2 )
    return (perimetro * apotema) / 2



def inicio():
    print('\n','1.-Calcular Area Triangulo', '\n',
          '\n','2.-Calcular Area Cuadrado', '\n',
          '\n','3.-Calcular Area Retangulo', '\n',
          '\n','4.-Calcular Area Hexagono', '\n',
          )
    opcion = input('Indique una opcion con el número que indica la operación: ')
    if opcion == '1':
        print(areaTriangulo())
    elif opcion == '2':
        print(areaCuadrado())
    elif opcion == '3':
        print(areaRetangulo())
    elif opcion == '4':
        print(areaHexagono())
    else:
        print("Indique una opcion correcta: ")
    vuelta()

def vuelta():
    nueva = input('Realizar otro calculo Si/No: ')

    if nueva == "Si" or nueva == "si":
        inicio()
    elif nueva =="No" or nueva == "no":
        print("Finalizado")
    else:
        print("Indique un valor correcto Si/No:")
        vuelta()

inicio()
