#./app/app.py
from flask import Flask
from markupsafe import escape
import random
import re
from flask import render_template



app = Flask(__name__)
# Pagina Principal
@app.route('/')
def hello_world():
  return 'Hello, World!'
# Pagina de error de enlace
@app.errorhandler(404)
def page_not_found(error):
    return 'Pagina no encontrada, verifique el enlace'
# Pagina estatica con imagen
@app.route('/estatica')
def gato():
    foto = '/static/images/gato.jpg alt="Gato"'
    return render_template('gato.html',foto=foto)
# Pagina con dibujos aleatorios
@app.route('/sgv')
def sgv():

    colores= ['red','green','blue', 'yellow','black']
    rectangulox = random.randint(0,500)
    rectanguloy = random.randint(0,500)
    recposx = random.randint(0,1000)
    recposy = random.randint(0,600)

    rectangulocol = random.choice(colores)
    elipsex = random.randint(0,500)
    elipsey = random.randint(0,500)
    elipsecol = random.choice(colores)


    return render_template('sgv.html',recposx=recposx, recposy=recposy,rectangulox=rectangulox,rectanguloy=rectanguloy,rectangulocol=rectangulocol,elipsex=elipsex,elipsey=elipsey,elipsecol=elipsecol)

# Pagina que ordena los numeros
@app.route('/ordena/<lista>')
def Burbuja(lista):
    numeros= lista.split(',')
    for numPasada in range(len(numeros)-1,0,-1):
        for i in range(numPasada):
            if numeros[i]>numeros[i+1]:
                temp = numeros[i]
                numeros[i] = numeros[i+1]
                numeros[i+1] = temp


    return f'La lista ordenada es : {numeros}'



# Pagina de criba de Eratostenes
@app.route('/criba/<int:numero>')
def criba(numero):
    lista = list(range(2,numero))
    for x in lista:
        for y in lista:
            if y%x == 0:
                lista.remove(y)
    lista.insert(0,2)
    return f'Los numeros primos menores de : {numero} son {lista}'

# Pagina de Fibonacci
@app.route('/fibonacci/<int:numero>')
def fibonacci(numero):
    resultado = [ 0 , 1]
    for i in range(1,numero):
        resultado.append(resultado[i] + resultado[i-1])
    return f'El numero {numero} en la sucesion fibonacci es : {resultado[numero]}'

# Pagina que indica si la cadena generada es valida
@app.route('/cadena')
def cadena():
    
    tamano = random.randint(2,10)
    resultado = []
    for i in range(0,tamano):
        if random.randint(0,1) == 0:
            resultado.append('[')
        else:
            resultado.append(']')

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
    if valido == True:
        return f'La cadena generada es {resultado} y es valida'
    else:
        return f'La cadena generada es {resultado} y es invalida'

# Pagina que indica si se ha indroducido un correo, un nombre, o una tarjeta valida
@app.route('/validacion/<cadena>')
def valido(cadena):
    if re.search('.+@\w+\.\w+', cadena):
        return f'La cadena introducida es un correo'
    if re.search('\d{4}-|\s\d{4}-|\s\d{4}-|\s\d{4}', cadena):
        return f'La cadena introducida es una tarjeta valida'
    if re.search('\w+\s\w', cadena):
        return f'La cadena introducida es un nombre'

    return f'la cadena introducida no corresponde a un correo,tarjeta valida o nombre'


def salir():
    return None