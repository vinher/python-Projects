import random
import time

marcas = ["ford","audi","mazda","renault","buggati","chevrolet"]
paises = ["mexico","argentina","españa","italia","alemania","hungria"]

print("Bienvenido al juego del ahorcado: ")
time.sleep(1)

print("Tienes que adivinar la palabra secreta\nTienes 5 oportunidades para intentar adivinar la palabra")
print("Jugar con Marcas de Autos o Países:")
time.sleep(2)
seleccion = input("Ingrese C Para Marcas de autos\nP Para paises")

while True:
    if seleccion.lower()=="c":
        print("Autos")
        palabra_secreta = random.choice(marcas)
        break
    elif seleccion.lower()=="p":
        print("Países")
        palabra_secreta = random.choice(paises)
        break
    else:
        print("Indique una categoria correcta: ")
        palabra_secreta = input("Ingrese una elección correcta: ")

op = 5
lista_letras_adivinar = []
print(' _ '  * len(palabra_secreta))

while True:
    while True:
        letra_adivinada = input("Adivina la letra: ")
        if(len(letra_adivinada) != 1 and letra_adivinada.isnumeric()):
            print("Intente ingresando una opción correcta: ")
        else:
            if letra_adivinada.lower() in lista_letras_adivinar:
                print("Ya intentaste con esa letra, prueba otra. ")
            else:
                lista_letras_adivinar.append(letra_adivinada)
                if letra_adivinada.lower() in palabra_secreta:
                    print(f"Felicidades Adivinaste La Letra:")
                    break
                else:
                    op = op-1
                    print("Perdiste una oportunidad")
                    print(f"Te quedan {op}  oportunidades: ")
                    break
    if op == 0:
        print(f"Perdiste la palabra secreta es: {palabra_secreta}")
        break
    estatus_actual = ""
    letras_faltantes = 0
    for letra in palabra_secreta:
        if letra in lista_letras_adivinar:
            estatus_actual = estatus_actual + letra

        else:
            estatus_actual = estatus_actual + "_"
            letras_faltantes = letras_faltantes + 1

    print(estatus_actual)

    if letras_faltantes == 0:
        print(f"Felicidades Haz Ganado\n La palabra secreta es: {palabra_secreta}")
        break
