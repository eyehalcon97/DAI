#./app/app.py

from flask import Flask , session ,request , render_template , jsonify
from flask import make_response , redirect , url_for
from flask_restful import reqparse, abort, Api, Resource
# pip install flask'resful

import random
import re
import model

app = Flask(__name__)
api = Api(app)
app.secret_key = "vjepmewawfew"

# Pagina Principal
@app.route('/')
def index():
    nombre = request.cookies.get('nombre')
    pagina = 'Home'
    link = 'index'
    visitado = leerhistorial()
    
    return enviarcookie(render_template('index.html',nombre=nombre,visitado=visitado),None,pagina,link)

# Pagina de error de enlace
@app.errorhandler(404)
def page_not_found(error):
    nombre = request.cookies.get('nombre')
    visitado = leerhistorial()
    solucion = 'Pagina no encontrada, por favor, verifique el enlace'
    return render_template('index.html',solucion=solucion,nombre=nombre,visitado=visitado)

# Pagina estatica con imagen
@app.route('/estatica')
def gato():
    nombre = request.cookies.get('nombre')
    pagina = 'Imagen Estatica'
    link = 'gato'
    visitado = leerhistorial()
    foto = '/static/images/gato.jpg alt="Gato" '
    return enviarcookie(render_template('gato.html',foto=foto,nombre=nombre,visitado=visitado),None,pagina,link)

@app.route('/entrar' , methods=['GET', 'POST'] )
def entrar():
    nombre = request.cookies.get('nombre')
    visitado = leerhistorial()
    if request.method == 'POST':
        nombre = request.form['nombre']
        pws = request.form['pws']
        
        if pws == model.leerbd(nombre):
            solucion = 'Bienvenido : ' + str(nombre)
            
            return enviarcookie(render_template('index.html',solucion=solucion,nombre=nombre,visitado=visitado),nombre)
        else: 
            if model.exiteuser(nombre):
                solucion = 'La contraseña es incorrecta'
                return render_template('entrar.html',solucion=solucion,visitado=visitado)
            else:
                solucion = 'Usuario o contraseña incorrecta'
                return render_template('entrar.html',solucion=solucion,visitado=visitado)
            
    else:
        if nombre == None:
            return render_template('entrar.html',visitado=visitado)
        else:
            solucion = 'El usuario ya esta logueado '
            return render_template('index.html',solucion=solucion,nombre=nombre,visitado=visitado)

@app.route('/registrar' , methods=['GET', 'POST'] )
def registrar():
    nombre = request.cookies.get('nombre')
    visitado = leerhistorial()
    if request.method == 'POST':
        nombre = request.form['nombre']
        psw = request.form['pws']
        
        if model.exiteuser(nombre):
            solucion = 'El usuario ya existe, Introduce un nuevo nombre de Usuario :'
            return render_template('registrar.html',solucion=solucion,visitado=visitado)
        else:
            if model.nuevousuario(nombre,psw):
                solucion = ' Se ha creado el usuario : ' + str(nombre)
                return enviarcookie(render_template('index.html',solucion=solucion,nombre=nombre,visitado=visitado),nombre)
    else:
        if nombre == None:
            solucion = 'Registro de nuevo usuario : '
            return render_template('registrar.html',solucion=solucion,visitado=visitado)
        else :
            solucion = 'El usuario ya esta logueado '
            return render_template('index.html',solucion=solucion,nombre=nombre,visitado=visitado)

@app.route('/modificar' , methods=['GET', 'POST'] )
def modificar():
    nombre = request.cookies.get('nombre')
    visitado = leerhistorial()
    password = model.leerbd(nombre)
    if request.method == 'POST':
        nombrenuevo = request.form['nombre']
        psw = request.form['pws']
        
        if nombre != nombrenuevo and model.exiteuser(nombrenuevo):
            solucion = 'El usuario ya existe, Introduce otro nombre de Usuario : '
            return render_template('modificar.html',solucion=solucion,visitado=visitado)
        else:
            if model.modificar(nombre,nombrenuevo,psw):
                nombre = nombrenuevo
                solucion = ' Se han modificado los datos del usuario : ' + str(nombre)
                return enviarcookie(render_template('index.html',solucion=solucion,nombre=nombre,visitado=visitado),nombre)
    else:
        if nombre == None:
            solucion = 'No ha iniciado Sesion'
            return render_template('modificar.html',solucion=solucion,visitado=visitado)
        else :
            solucion = 'Modifique el Usuario '
            return render_template('modificar.html',solucion=solucion,nombre=nombre,psw=password,visitado=visitado)

@app.route('/pedirdatos/<cadena>' , methods=['GET', 'POST'] )
def pedirdatos(cadena):
    nombre = request.cookies.get('nombre')
    pagina = 'Pedir datos de : ' + str(cadena)
    link = 'pedirdatos'
    visitado = leerhistorial()
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
        return enviarcookie(render_template('pedirdatos.html',cadena=cadena,nombre=nombre,visitado=visitado),None,pagina,link,cadena)

# Pagina que ordena los numeros
@app.route('/ordena/<cadena>')
def burbuja(cadena):
    nombre = request.cookies.get('nombre')
    pagina = 'Ordena : ' + str(cadena)
    link = 'burbuja'
    visitado = leerhistorial()
    numeros= cadena.split(',')
    for numPasada in range(len(numeros)-1,0,-1):
        for i in range(numPasada):
            if numeros[i]>numeros[i+1]:
                temp = numeros[i]
                numeros[i] = numeros[i+1]
                numeros[i+1] = temp


    solucion = 'La lista ordenada es : ' + str(numeros)
    return enviarcookie(render_template('index.html',solucion=solucion,nombre=nombre,visitado=visitado),None,pagina,link,cadena)

# Pagina de criba de Eratostenes
@app.route('/criba/<cadena>')
def criba(cadena):
    nombre = request.cookies.get('nombre')
    pagina = 'Criba : ' + str(cadena)
    link = 'criba'
    visitado = leerhistorial()
    lista = list(range(2,int(cadena)))
    for x in lista:
        for y in lista:
            if y%x == 0:
                lista.remove(y)
    lista.insert(0,2)
    solucion = 'Los numeros primos menores de : ' + cadena + ' son ' + str(lista) 
    return enviarcookie(render_template('index.html',solucion=solucion,nombre=nombre,visitado=visitado),None,pagina,link,cadena)

# Pagina de Fibonacci
@app.route('/fibonacci/<cadena>')
def fibonacci(cadena):
    nombre = request.cookies.get('nombre')
    pagina = 'fibbonacci : ' + str(cadena)
    link = 'fibonacci'
    visitado = leerhistorial()
    resultado = [ 0 , 1]
    for i in range(1,int(cadena)):
        resultado.append(resultado[i] + resultado[i-1])
    solucion = 'El numero ' + cadena + ' en la sucesion fibonacci es :' + str(resultado[int(cadena)])
    return enviarcookie(render_template('index.html',solucion=solucion,nombre=nombre,visitado=visitado),None,pagina,link,cadena)

# Pagina que indica si la cadena generada es valida
@app.route('/cadena')
def cadena():
    nombre = request.cookies.get('nombre')
    pagina = 'Cadena'
    link = 'cadena'
    visitado = leerhistorial()
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

    return enviarcookie(render_template('index.html',solucion=solucion,nombre=nombre,visitado=visitado),None,pagina,link)

# Pagina que indica si se ha indroducido un correo, un nombre, o una tarjeta valida
@app.route('/validacion/<cadena>')
def valido(cadena):
    nombre = request.cookies.get('nombre')
    pagina = 'Validacion de : ' + str(cadena)
    link = 'valido'
    visitado = leerhistorial()
    if re.search('.+@\w+\.\w+', cadena):
        solucion = 'La cadena introducida es un correo'
    elif re.search('\d{4}-|\s\d{4}-|\s\d{4}-|\s\d{4}', cadena):
        solucion = 'La cadena introducida es una tarjeta valida'
    elif re.search('\w+\s\w', cadena):
        solucion = 'La cadena introducida es un nombre'
    else :
        solucion = 'la cadena introducida no corresponde a un correo,tarjeta valida o nombre'

    return enviarcookie(render_template('index.html',solucion=solucion,nombre=nombre,visitado=visitado),None,pagina,link,cadena)



@app.route('/pokedex/<cadena>' , methods=['GET'] )
def pokedex(cadena):

    cadenasplit = cadena.split('.')
    
    nombre = request.cookies.get('nombre')
    link = 'pokedex'
    numero = int(cadenasplit[2])
    visitado = leerhistorial()
    if cadenasplit[1] == 'busqueda':
        pokedex = model.busquedapokedex(cadenasplit[0])
        pagina = 'pokedex Busqueda : ' + cadenasplit[0] + ' Pagina : ' + str(numero)
        if(len(pokedex) == 0):
            solucion = 'No se ha encontrado nada con el argumento : ' + cadenasplit[0]
            pagina = 'pokedex Busqueda : ' + cadenasplit[0]

        else:
            solucion = 'Se ha encontrado los siguientes elementos con el argumento : ' + cadenasplit[0]
        
    else:
        
        pokedex = model.BDpokedex()
        pagina = 'pokedex Pagina : ' + str(numero)
        solucion=''
    
    siguiente =  cadenasplit[0] + '.' + cadenasplit[1] + '.' + str(numero+1)
    atras = -1
    paginas = []
    tamanio = len(pokedex)
    if(numero > 0):
        atras = cadenasplit[0] + '.' + cadenasplit[1] + '.' + str(numero-1)
    if((numero+1)*6 >= tamanio):
        siguiente=0
    j=0
    for i in range(0,tamanio,6):
        paginas.append( {'valor' : cadenasplit[0] + '.' + cadenasplit[1] + '.' + str(j) ,'numero' : j})
        j=j+1
    
    pokedex = pokedex[numero*6:numero*6+6]
    paginado = numero
    pokemon = 1
    return enviarcookie(render_template('index.html',pokedex=pokedex,pokemon=pokemon,nombre=nombre,solucion=solucion,paginado=paginado,paginas=paginas,siguiente=siguiente,atras=atras,visitado=visitado),None,pagina,link,cadena)






	

@app.route('/salir')
def salir():
    visitado = leerhistorial()
    solucion = 'Se ha salido de la sesion'
    
    return enviarcookie(render_template('index.html',solucion=solucion,visitado=visitado),0)







def enviarcookie(respuesta,user=None,nombrepag=None,link=None,datos=None):
    resp = make_response(respuesta)
    if user != None:
        if user == 0:
            resp.set_cookie('nombre',expires=0)
        else:
            resp.set_cookie('nombre',user)
    if nombrepag != None and link != None:
        if(datos != None):
            clave = str(nombrepag) + '+' + str(link) + '+' + str(datos)
        else:
            clave = str(nombrepag) + '+' + str(link)
        cookie0 = request.cookies.get('visitado0')
        cookie1 = request.cookies.get('visitado1')
        cookie2 = request.cookies.get('visitado2')
        if cookie0 == None:
            resp.set_cookie('visitado0',clave)
        elif cookie1 == None:
            resp.set_cookie('visitado1',clave)
        elif cookie2 == None :
            resp.set_cookie('visitado2',clave)
        else :
            resp.set_cookie('visitado2', cookie1)
            resp.set_cookie('visitado1', cookie0)
            resp.set_cookie('visitado0', clave)
    return resp

def leerhistorial():
    resp = []
    cookie0 = request.cookies.get('visitado0')
    cookie1 = request.cookies.get('visitado1')
    cookie2 = request.cookies.get('visitado2')
    if cookie0 != None:
        cadena = cookie0.split('+')
        if len(cadena) == 3:
            cookie = {'nombre':cadena[0],'link':cadena[1],'dato':cadena[2]}
        else:
            cookie = {'nombre':cadena[0],'link':cadena[1]}
        resp.append(cookie)
        if cookie1 != None:
            cadena = cookie1.split('+')
            if len(cadena) == 3:
                cookie = {'nombre':cadena[0],'link':cadena[1],'dato':cadena[2]}
            else:
                cookie = {'nombre':cadena[0],'link':cadena[1]}
            resp.append(cookie)
            if cookie2 != None:
                cadena = cookie2.split('+')
                if len(cadena) == 3:
                    cookie = {'nombre':cadena[0],'link':cadena[1],'dato':cadena[2]}
                else:
                    cookie = {'nombre':cadena[0],'link':cadena[1]}
                resp.append(cookie)
    return resp



@app.route('/pokedexAPI/<pokemon_id>' ,  methods=['GET', 'POST', 'DELETE', 'PUT'])  
def pokemon(pokemon_id):
    if request.method == 'GET':
        if (model.exits(pokemon_id)):
            return model.busquedapokedexjson(pokemon_id)
        else:
            resp = jsonify({"detalles": "No se encontro el pokemon con el argumento : " +  pokemon_id})
            resp.status_code = 400 # aquí cambiamos el código de estado a 400 (código muy común en caso de errores de solicitud)
            return resp
    if request.method == 'DELETE':
        if (model.exits(pokemon_id)):
            return model.eliminarpokemon(pokemon_id)
        else:
            resp = jsonify({"detalles": "No se pudo borrar el pokemon : " +  pokemon_id})
            resp.status_code = 400 # aquí cambiamos el código de estado a 400 (código muy común en caso de errores de solicitud)
            return resp
    if request.method == 'POST':
        data = request.get_json()
        return model.addpokemon(data)
    
    if request.method == 'PUT':
        data = request.get_json()
        return model.modpokemon(pokemon_id,data)
        

##
## Actually setup the Api resource routing here
##
