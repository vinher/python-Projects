#Tablas de multiplicar
#19-10-21
#tecnologias:Python
def multiplicar():
    var = int(input("Ingresa el numero de la tabla que quieres hacer: "))

    for p in range(10):
        print(f"{var} X {p + 1} = ",p * var + var)

    op = input("Quiere saber otra tabla de multiplicar: Si/No: ")

    if op == "Si" or op == "si":
        multiplicar()
    elif op == "No" or op == "no":
        print("Programa Finalizado")
    else:
        print("Indique una opcion correcta")
        multiplicar()

multiplicar()
