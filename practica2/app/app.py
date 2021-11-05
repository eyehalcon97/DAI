#./app/app.py

from flask import Flask , session ,request , render_template
from flask import make_response

import random
import re
import model

app = Flask(__name__)
app.secret_key = "vjepmewawfew"

# Pagina Principal
@app.route('/')
def index():
    nombre = request.cookies.get('nombre')
    
    
    return historial(render_template('index.html',nombre=nombre))

# Pagina de error de enlace
@app.errorhandler(404)
def page_not_found(error):
    nombre = request.cookies.get('nombre')
    solucion = 'Pagina no encontrada, por favor, verifique el enlace'
    #visitado = ultimavisita('error','','','')
    return render_template('index.html',solucion=solucion,nombre=nombre)

# Pagina estatica con imagen
@app.route('/estatica')
def gato():
    nombre = request.cookies.get('nombre')
    #visitado = ultimavisita('estatica','gato','')
    foto = '/static/images/gato.jpg alt="Gato"'
    return render_template('gato.html',foto=foto,nombre=nombre)

@app.route('/entrar' , methods=['GET', 'POST'] )
def entrar():
    nombre = request.cookies.get('nombre')
    #visitado = ultimavisita('entrar','entrar','')
    if request.method == 'POST':
        nombre = request.form['nombre']
        pws = request.form['pws']
        
        if pws == model.leerbd(nombre):
            solucion = 'Bienvenido : ' + str(nombre)
            
            
            return historial(render_template('index.html',solucion=solucion,nombre=nombre),nombre)
        else: 
            if model.exiteuser(nombre):
                solucion = 'La contraseña es incorrecta'
                return historial( render_template('entrar.html',solucion=solucion))
            else:
                solucion = 'El usuario no existe'
                return historial(render_template('entrar.html',solucion=solucion))
            
    else:
        if nombre == None:
            return historial(render_template('entrar.html'),'')
        else:
            solucion = 'El usuario ya esta logueado '
            return historial(render_template('index.html',solucion=solucion,nombre=nombre))

@app.route('/registrar' , methods=['GET', 'POST'] )
def registrar():
    nombre = request.cookies.get('nombre')
    #visitado = ultimavisita('registrar','registrar','')
    if request.method == 'POST':
        nombre = request.form['nombre']
        psw = request.form['pws']
        
        if model.exiteuser(nombre):
            solucion = 'El usuario ya existe, Introduce un nuevo nombre de Usuario :'
            return render_template('registrar.html',solucion=solucion)
        else:
            if model.nuevousuario(nombre,psw):
                solucion = ' Se ha creado el usuario : ' + str(nombre)
                resp = make_response(render_template('index.html',solucion=solucion,nombre=nombre))
                resp.set_cookie('nombre',nombre)
                return resp
    else:
        if nombre == None:
            solucion = 'Registro de nuevo usuario : '
            return render_template('registrar.html',solucion=solucion)
        else :
            solucion = 'El usuario ya esta logueado '
            return render_template('index.html',solucion=solucion,nombre=nombre)

@app.route('/modificar' , methods=['GET', 'POST'] )
def modificar():
    nombre = request.cookies.get('nombre')
    password = model.leerbd(nombre)
    if request.method == 'POST':
        nombrenuevo = request.form['nombre']
        psw = request.form['pws']
        
        if nombre != nombrenuevo and model.exiteuser(nombrenuevo):
            solucion = 'El usuario ya existe, Introduce otro nombre de Usuario : '
            return historial(render_template('modificar.html',solucion=solucion))
        else:
            if model.modificar(nombre,nombrenuevo,psw):
                nombre = nombrenuevo
                solucion = ' Se han modificado los datos del usuario : ' + str(nombre)
                #resp = make_response(render_template('index.html',solucion=solucion,nombre=nombre))
                #resp.set_cookie('nombre',nombre)
                return historial(render_template('index.html',solucion=solucion,nombre=nombre),nombre)
    else:
        if nombre == None:
            solucion = 'No ha iniciado Sesion'
            return historial(render_template('modificar.html',solucion=solucion))
        else :
            solucion = 'Modifique el Usuario '
            return historial(render_template('modificar.html',solucion=solucion,nombre=nombre,psw=password),nombre)

@app.route('/pedirdatos/<cadena>' , methods=['GET', 'POST'] )
def pedirdatos(cadena):
    nombre = request.cookies.get('nombre')
    #visitado = ultimavisita('pedirdatos','pedirdatos',cadena)
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
        return render_template('pedirdatos.html',cadena=cadena,nombre=nombre)


# Pagina con dibujos aleatorios
@app.route('/sgv')
def sgv():
    nombre = request.cookies.get('nombre')
    #visitado = ultimavisita('sgv','sgv','')
    colores= ['red','green','blue', 'yellow','black']
    rectangulox = random.randint(0,500)
    rectanguloy = random.randint(0,500)
    recposx = random.randint(0,1000)
    recposy = random.randint(0,600)
    rectangulocol = random.choice(colores)
    elipsex = random.randint(0,500)
    elipsey = random.randint(0,500)
    elipsecol = random.choice(colores)
    return render_template('sgv.html',recposx=recposx, recposy=recposy,rectangulox=rectangulox,rectanguloy=rectanguloy,rectangulocol=rectangulocol,elipsex=elipsex,elipsey=elipsey,elipsecol=elipsecol,nombre=nombre)

# Pagina que ordena los numeros
@app.route('/ordena/<cadena>')
def burbuja(cadena):
    nombre = request.cookies.get('nombre')
    #visitado = ultimavisita('ordena','burbuja',cadena)
    numeros= cadena.split(',')
    for numPasada in range(len(numeros)-1,0,-1):
        for i in range(numPasada):
            if numeros[i]>numeros[i+1]:
                temp = numeros[i]
                numeros[i] = numeros[i+1]
                numeros[i+1] = temp


    solucion = 'La lista ordenada es : ' + str(numeros)
    return render_template('index.html',solucion=solucion,nombre=nombre)

# Pagina de criba de Eratostenes
@app.route('/criba/<cadena>')
def criba(cadena):
    nombre = request.cookies.get('nombre')
    #visitado = ultimavisita('criba','criba',cadena)
    lista = list(range(2,int(cadena)))
    for x in lista:
        for y in lista:
            if y%x == 0:
                lista.remove(y)
    lista.insert(0,2)
    solucion = 'Los numeros primos menores de : ' + cadena + ' son ' + str(lista) 
    return render_template('index.html',solucion=solucion,nombre=nombre)

# Pagina de Fibonacci
@app.route('/fibonacci/<cadena>')
def fibonacci(cadena):
    nombre = request.cookies.get('nombre')
    #visitado = ultimavisita('fibonacci','fibonacci',cadena)
    resultado = [ 0 , 1]
    for i in range(1,int(cadena)):
        resultado.append(resultado[i] + resultado[i-1])
    solucion = 'El numero ' + cadena + ' en la sucesion fibonacci es :' + str(resultado[int(cadena)])
    return render_template('index.html',solucion=solucion,nombre=nombre)

# Pagina que indica si la cadena generada es valida
@app.route('/cadena')
def cadena():
    nombre = request.cookies.get('nombre')
    #visitado = ultimavisita('cadena','cadena','')
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

    return render_template('index.html',solucion=solucion,nombre=nombre)

# Pagina que indica si se ha indroducido un correo, un nombre, o una tarjeta valida
@app.route('/validacion/<cadena>')
def valido(cadena):
    nombre = request.cookies.get('nombre')
    #visitado = ultimavisita('validacion','valido',cadena)
    if re.search('.+@\w+\.\w+', cadena):
        solucion = 'La cadena introducida es un correo'
    elif re.search('\d{4}-|\s\d{4}-|\s\d{4}-|\s\d{4}', cadena):
        solucion = 'La cadena introducida es una tarjeta valida'
    elif re.search('\w+\s\w', cadena):
        solucion = f'La cadena introducida es un nombre'
    else :
        solucion = f'la cadena introducida no corresponde a un correo,tarjeta valida o nombre'

    return render_template('index.html',solucion=solucion,nombre=nombre)

@app.route('/salir')
def salir():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('nombre', expires=0)
    return resp

def historial(respuesta,user=None,visitado=None,datos=None):
    resp = make_response(respuesta)
    if user != None:
        resp.set_cookie('nombre',user)
    if visitado != None:
        clave = {"nombre":visitado[0],"link":visitado[1],"dato":datos}
    
    cookie = []
    cookie.append(request.cookies.get('visitado0'))
    cookie.append(request.cookies.get('visitado1'))
    cookie.append(request.cookies.get('visitado2'))
    
    if len(cookie) == 0:
        resp.set_cookie('visitado0',clave)
    elif len(cookie) == 1:
        resp.set_cookie('visitado1',clave)
    elif len(cookie) == 2:
        resp.set_cookie('visitado2',clave)
    elif len(cookie) == 3:
        resp.set_cookie('visitado2', cookie[1])
        resp.set_cookie('visitado1', cookie[0])
        resp.set_cookie('visitado0', clave)
    return resp

