
from pymongo import MongoClient

client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
db = client.SampleCollections        # Elegimos la base de datos de ejemplo


def nuevousuario(nombre,psw):
    
   #db[nombre] = {'psw':psw}
    return True

def leerbd(nombre):
    #return db[nombre]['psw']
    return True

def exiteuser(nombre):
    #if nombre in db:
    #    return True
    #else:
    return False

def modificar(nombre,nombrenuevo,psw):
    #db[nombrenuevo] = db[nombre]
    #del db[nombre]
    #db[nombrenuevo] = {'psw':psw}
    return True


def BDfriends():
	# Encontramos los documentos de la coleccion "samples_friends"
    episodios = db.samples_friends.find() # devuelve un cursor(*), no una lista ni un iterador
    
    lista_episodios = []
    for episodio in episodios:
        lista_episodios.append(episodio)

    return lista_episodios


def BDfri(min , max):
    
    episodios = db.samples_friends.find() # devuelve un cursor(*), no una lista ni un iterador
    
    lista_episodios = []
    for episodio in episodios:
        lista_episodios.append(episodio)

    return lista_episodios[min:max]

def lenfriends():
    episodios = db.samples_friends.find() # devuelve un cursor(*), no una lista ni un iterador
    lista_episodios = []
    for episodio in episodios:
        lista_episodios.append(episodio)

    return len(lista_episodios)

def busquedafriends(nombre):
    if nombre.isdigit():
        episodios = db.samples_friends.find({ "$or": [{"season": float(nombre)}, {"number": float(nombre)} ]})     # devuelve un cursor(*), no una lista ni un iterador
    else:
        episodios = db.samples_friends.find({ "$or": [{"name": {"$regex": nombre}}, {"summary": {"$regex": nombre}} ]})     # devuelve un cursor(*), no una lista ni un iterador

    lista_episodios = []
    for episodio in episodios:
        lista_episodios.append(episodio)

    return episodios

def busquedapokedex(nombre):
    if nombre.isdigit():
        pokedex = db.samples_pokemon.find({ "$or": [ {"id": float(nombre)}, {"num": float(nombre)}    ]})     # devuelve un cursor(*), no una lista ni un iterador
    else:
        nombre = nombre.capitalize()
        pokedex = db.samples_pokemon.find({ "$or": [{"name": {"$regex": nombre}}, {"type": {"$regex": nombre}}   ]})     # devuelve un cursor(*), no una lista ni un iterador
    
    lista_pokemon = []
    for pokemon in pokedex:
        lista_pokemon.append(pokemon)

    return lista_pokemon


def BDpokedex():
	# Encontramos los documentos de la coleccion "samples_friends"
    pokedex = db.samples_pokemon.find() # devuelve un cursor(*), no una lista ni un iterador
    
    lista_pokemon = []
    for pokemon in pokedex:
        lista_pokemon.append(pokemon)

    return lista_pokemon
	# a los templates de Jinja hay que pasarle una lista, no el cursor
	

def BDpoke(min , max):
    pokedex = db.samples_pokemon.find() # devuelve un cursor(*), no una lista ni un iterador
    
    lista_pokemon = []
    for pokemon in pokedex:
        lista_pokemon.append(pokemon)

    return lista_pokemon[min:max]

def lenpokedex():
    pokedex = db.samples_pokemon.find() # devuelve un cursor(*), no una lista ni un iterador
    lista_pokemon = []
    for pokemon in pokedex:
        lista_pokemon.append(pokemon)

    return len(lista_pokemon)