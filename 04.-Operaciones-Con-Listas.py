#Descripción realizar operaciones de las listas tuplas o diccionarios con ciclos for
#while

lista1 = [1,2,3,4,5,6,7,8,9,10]
position1 = 0
lista2 = [20,19,18,17,16,15,14,13,12,11]
position2 = 0
#MULTIPLICACIÓN
print("MULTIPLICACIÓN")
#FUNCION LEN NOS AYUDA A SABER EL TAMAÑO DE UNA LISTA
for p in range(len(lista1)):
    op = lista1[p] * lista2[p]
    print(f"Operación en posición {p + 1 }: ",lista1[p]," x ",lista2[p]," = ", op)

#DIVISION
print("DIVISION")
for p in range(len(lista1)):
    op = lista1[p] / lista2[p]
    print(f"Operación en posición {p + 1 }: ",lista1[p]," / ",lista2[p]," = ", op)

#RESTA
print("RESTA")
for p in range(len(lista1)):
    op = lista1[p] - lista2[p]
    print(f"Operación en posición {p + 1 }: ",lista1[p]," - ",lista2[p]," = ", op)

#SUMA
print("SUMA")
for p in range(len(lista1)):
    op = lista1[p] + lista2[p]
    print(f"Operación en posición {p + 1 }: ",lista1[p]," + ",lista2[p]," = ", op)

#MODULO
print("MODULO")
for p in range(len(lista1)):
    op = lista1[p] % lista2[p]
    print(f"Operación en posición {p + 1 }: ",lista1[p]," % ",lista2[p]," = ", op)
