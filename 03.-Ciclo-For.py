#Tema:Ejercicios con el ciclo for y la función range
#Ejercicios Sacados de la pagina https://aprendeconalf.es/docencia/python/ejercicios/bucles/

#Mi Solución
print("Se imprimiera 10 veces")
var = input("Ingrese una palabra: ")
var1 = [1,2,3,4,5,6,7,8,9,10]
for v in var1:
    print(var)

#Solución 2
print("Se imprimiera 10 veces")
word = input("Ingrese una palabra: ")
for i in range(10):
    print(word)

#Edad
print("Imprimira la edad del 1 hasta los años que tengas")
age = int(input("Ingrese Su Edad"))
for i in range(age):
    print(i+1)
#Numeros Impares
print("Imprimira numeros impares")
num = int(input("Ingrese un número entero: "))
for i in range(num):
    if i % 2 !=0:
        print(i)

#Cuenta Regresiva
print("Imprimira la cuenta regresiva de los numeros")
num = int(input("Ingrese un número: "))
for i in range(1,num + 1):
    print(" ",num-i + 1)

#Cuenta Regresiva con numeros impares
print("Imprimira numeros impares de manera desendente: ")
des = int(input("Ingrese un numero: "))
for i in range(1,des +1):
    if i % 2 !=0:
        print(" ",des-i)
