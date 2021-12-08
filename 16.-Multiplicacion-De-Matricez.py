#Multiplicación de Matricez
#1.-Ingresar la función.
# Identificar las letras
#2.-Llenar la matriz y la estrcutura
#3.-Comenzar a multiplicar las posiciones de las listas(Matriz)
var = input("Indique su función: ")
print(f'{var}')
lista = list(var)
print(lista)

lista1 = [0,0,0,0,0,0,0,0,0]
for i in range(9):
    var = input("Llene su matriz posicion ")
    lista1[i] = var
    print(lista1)
