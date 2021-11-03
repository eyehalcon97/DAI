#./app/app.py
from flask import Flask
from flask.wrappers import Request
from markupsafe import escape
import random
from flask import request
import re
from flask import render_template

app = Flask(__name__)
# Pagina Principal
@app.route('/')
def index():
  return render_template('index.html')

# Pagina de error de enlace
@app.errorhandler(404)
def page_not_found(error):
    return 'Pagina no encontrada, verifique el enlace'

# Pagina estatica con imagen
@app.route('/estatica')
def gato():
    foto = '/static/images/gato.jpg alt="Gato"'
    return render_template('gato.html',foto=foto)


@app.route('/pedirdatos/<ejercicio>' , methods=['GET', 'POST'] )
def pedirdatos(ejercicio):
        if request.method == 'POST':
            datos = request.form['datos']
            if ejercicio == 'ordenacion':
                return burbuja(datos)
            elif ejercicio == 'criba':
                return criba(datos)
            elif ejercicio == 'fibonacci':
                return fibonacci(datos)
            elif ejercicio == 'cadena':
                return valido(datos)

        else:    
            return render_template('pedirdatos.html',ejercicio=ejercicio)


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
def burbuja(lista):
    numeros= lista.split(',')
    for numPasada in range(len(numeros)-1,0,-1):
        for i in range(numPasada):
            if numeros[i]>numeros[i+1]:
                temp = numeros[i]
                numeros[i] = numeros[i+1]
                numeros[i+1] = temp


    solucion = 'La lista ordenada es : ' + str(numeros)
    return render_template('resultado.html',solucion=solucion)

# Pagina de criba de Eratostenes
@app.route('/criba/<numero>')
def criba(numero):
    lista = list(range(2,int(numero)))
    for x in lista:
        for y in lista:
            if y%x == 0:
                lista.remove(y)
    lista.insert(0,2)
    solucion = 'Los numeros primos menores de : ' + numero + ' son ' + str(lista) 
    return render_template('resultado.html',solucion=solucion)

# Pagina de Fibonacci
@app.route('/fibonacci/<numero>')
def fibonacci(numero):
    resultado = [ 0 , 1]
    for i in range(1,int(numero)):
        resultado.append(resultado[i] + resultado[i-1])
    solucion = 'El numero ' + numero + ' en la sucesion fibonacci es :' + str(resultado[int(numero)])
    return render_template('resultado.html',solucion=solucion)

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
            valor=valor-1
            if valor<0:
                valido = False
    if valor != 0:
        valido = False

        if valido == True:
            solucion = 'La cadena generada es ' + str(resultado) + ' y es valida'
        else:
            solucion ='La cadena generada es ' + str(resultado) + ' y es invalida'

    return render_template('resultado.html',solucion=solucion)

# Pagina que indica si se ha indroducido un correo, un nombre, o una tarjeta valida
@app.route('/validacion/<cadena>')
def valido(cadena):
    if re.search('.+@\w+\.\w+', cadena):
        solucion = 'La cadena introducida es un correo'
    elif re.search('\d{4}-|\s\d{4}-|\s\d{4}-|\s\d{4}', cadena):
        solucion = 'La cadena introducida es una tarjeta valida'
    elif re.search('\w+\s\w', cadena):
        solucion = f'La cadena introducida es un nombre'
    else :
        solucion = f'la cadena introducida no corresponde a un correo,tarjeta valida o nombre'

    return render_template('resultado.html',solucion=solucion)