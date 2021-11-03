#./app/app.py
from flask import Flask

from markupsafe import escape
import random
from flask import request
import re
from flask import render_template

app = Flask(__name__)

visitado = []
# Pagina Principal
@app.route('/')
def index():
    ultimavisita('Home','index','')
    return render_template('index.html',visitado=visitado)

# Pagina de error de enlace
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html',visitado=visitado)

# Pagina estatica con imagen
@app.route('/estatica')
def gato():
    ultimavisita('estatica','gato','')
    foto = '/static/images/gato.jpg alt="Gato"'
    return render_template('gato.html',foto=foto,visitado=visitado)

@app.route('/entrar' , methods=['GET', 'POST'] )
def entrar():
    ultimavisita('entrar','entrar','')
    if request.method == 'POST':
        nombreusuario = request.form['nombre']
        pws = request.form['pws']
        return f'hola ' + nombreusuario
    return render_template('entrar.html',visitado=visitado)

@app.route('/registrar' , methods=['GET', 'POST'] )
def registrar():
    ultimavisita('registrar','registrar','')
    if request.method == 'POST':
        nombreusuario = request.form['nombre']
        pws = request.form['pws']
        return f'hola ' + nombreusuario
    return render_template('registrar.html',visitado=visitado)


@app.route('/pedirdatos/<cadena>' , methods=['GET', 'POST'] )
def pedirdatos(cadena):
    ultimavisita('pedirdatos','pedirdatos',cadena)
    if request.method == 'POST':
        datos = request.form['datos']
        if cadena == 'ordenacion':
            return burbuja(datos)
        elif cadena == 'criba':
            return criba(datos)
        elif cadena == 'fibonacci':
            return fibonacci(datos)
        elif cadena == 'cadena':
            return valido(datos)

    else:    
        return render_template('pedirdatos.html',cadena=cadena,visitado=visitado)


# Pagina con dibujos aleatorios
@app.route('/sgv')
def sgv():
    ultimavisita('sgv','sgv','')
    colores= ['red','green','blue', 'yellow','black']
    rectangulox = random.randint(0,500)
    rectanguloy = random.randint(0,500)
    recposx = random.randint(0,1000)
    recposy = random.randint(0,600)
    rectangulocol = random.choice(colores)
    elipsex = random.randint(0,500)
    elipsey = random.randint(0,500)
    elipsecol = random.choice(colores)
    return render_template('sgv.html',recposx=recposx, recposy=recposy,rectangulox=rectangulox,rectanguloy=rectanguloy,rectangulocol=rectangulocol,elipsex=elipsex,elipsey=elipsey,elipsecol=elipsecol,visitado=visitado)

# Pagina que ordena los numeros
@app.route('/ordena/<cadena>')
def burbuja(cadena):
    ultimavisita('ordena','burbuja',cadena)
    numeros= cadena.split(',')
    for numPasada in range(len(numeros)-1,0,-1):
        for i in range(numPasada):
            if numeros[i]>numeros[i+1]:
                temp = numeros[i]
                numeros[i] = numeros[i+1]
                numeros[i+1] = temp


    solucion = 'La lista ordenada es : ' + str(numeros)
    return render_template('resultado.html',solucion=solucion,visitado=visitado)

# Pagina de criba de Eratostenes
@app.route('/criba/<cadena>')
def criba(cadena):
    ultimavisita('criba','criba',cadena)
    lista = list(range(2,int(cadena)))
    for x in lista:
        for y in lista:
            if y%x == 0:
                lista.remove(y)
    lista.insert(0,2)
    solucion = 'Los numeros primos menores de : ' + cadena + ' son ' + str(lista) 
    return render_template('resultado.html',solucion=solucion,visitado=visitado)

# Pagina de Fibonacci
@app.route('/fibonacci/<cadena>')
def fibonacci(cadena):
    ultimavisita('fibonacci','fibonacci',cadena)
    resultado = [ 0 , 1]
    for i in range(1,int(cadena)):
        resultado.append(resultado[i] + resultado[i-1])
    solucion = 'El numero ' + cadena + ' en la sucesion fibonacci es :' + str(resultado[int(cadena)])
    return render_template('resultado.html',solucion=solucion,visitado=visitado)

# Pagina que indica si la cadena generada es valida
@app.route('/cadena')
def cadena():
    ultimavisita('cadena','cadena','')
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
            valor=valor-1
            if valor<0:
                valido = False
    if valor != 0:
        valido = False

    if valido == True:
        solucion = 'La cadena generada es ' + str(resultado) + ' y es valida'
    else:
        solucion ='La cadena generada es ' + str(resultado) + ' y es invalida'

    return render_template('resultado.html',solucion=solucion,visitado=visitado)

# Pagina que indica si se ha indroducido un correo, un nombre, o una tarjeta valida
@app.route('/validacion/<cadena>')
def valido(cadena):
    ultimavisita('validacion','valido',cadena)
    if re.search('.+@\w+\.\w+', cadena):
        solucion = 'La cadena introducida es un correo'
    elif re.search('\d{4}-|\s\d{4}-|\s\d{4}-|\s\d{4}', cadena):
        solucion = 'La cadena introducida es una tarjeta valida'
    elif re.search('\w+\s\w', cadena):
        solucion = f'La cadena introducida es un nombre'
    else :
        solucion = f'la cadena introducida no corresponde a un correo,tarjeta valida o nombre'

    return render_template('resultado.html',solucion=solucion,visitado=visitado)

def ultimavisita(nombre,link,dato):
    valor = ({"link":link,"dato":dato})
    numero = len(visitado)
    if numero < 3:
        visitado.append({"nombre":nombre,"enlace":valor})
    else :
        visitado[2] = visitado[1]
        visitado[1] = visitado[0]
        visitado[0] = {"nombre":nombre,"enlace":valor}
    return None