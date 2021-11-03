# ejercicios/cadena.py

import random

tamano = random.randint(2,10)
resultado = []
for i in range(0,tamano):
    if random.randint(0,1) == 0:
        resultado.append('[')
    else:
        resultado.append(']')
    
print("La cadena generada es :")
print(resultado)

valor=0
valido=True

for i in resultado:
    if i == '[':
        valor=valor+1
    else: 
        i == ']'
        valor=valor-1
        if valor<0:
            valido = False

print("la cadena es :")
if valido == True:
    print("Correcto")
else:
    print("Incorrecto")
