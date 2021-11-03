# ejercicios/criba.py

print("Introduzca un numero mayor o igual que 2: ")
numero = int(input())
lista = list(range(2,numero))
print(lista)
for x in lista:
    for y in lista:
        if y%x == 0:
            lista.remove(y)
lista.insert(0,2)
    

print("Los numeros primos comprendidos entre 2 y ")
print(numero)
print(" son :")
print(lista)