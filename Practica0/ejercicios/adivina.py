# ejercicios/adivina.py
import random

numero = random.randint(0,100)

print("Introduzca un numero : ")
introduce = int(input())
while numero != introduce:
    if numero < introduce:
        print("El numero es menor")
    else:
        print("El numero es mayor")

    print("Introduzca un numero : ")
    introduce = int(input())

print("El numero era: ")
print(numero)
print("Felicidades, has acertado!!")

