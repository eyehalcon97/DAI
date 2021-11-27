
from pymongo import MongoClient
from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource



client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
db = client.SampleCollections        # Elegimos la base de datos de ejemplo



parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('_id')
parser.add_argument('id')
parser.add_argument('num')
parser.add_argument('img')
parser.add_argument('type')
parser.add_argument('height')
parser.add_argument('candy')
parser.add_argument('egg')
parser.add_argument('spawn_chance')
parser.add_argument('avg_spawns')
parser.add_argument('spawn_time')
parser.add_argument('multipliers')
parser.add_argument('weaknesses')


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
	
def eliminarpokemon(nombre):
    if nombre.isdigit():
        db.samples_pokemon.remove({ "$or": [ {"id": float(nombre)}, {"num": float(nombre)}    ]})     # devuelve un cursor(*), no una lista ni un iterador
    else:
        nombre = nombre.capitalize()
        db.samples_pokemon.remove({ "$or": [{"name": {"$regex": nombre}}, {"type": {"$regex": nombre}}   ]})    # devuelve un cursor(*), no una lista ni un iterador
    
    return None




def addpokemon(data):

    db.samples_pokemon_insert(data)
    return busquedapokedexjson(data["name"])


def modpokemon(valor):
    args = parser.parse_args()
    return valor



def exits(nombre):
    if nombre.isdigit():
        pokedex = db.samples_pokemon.find({ "$or": [ {"id": float(nombre)}, {"num": float(nombre)}    ]})     # devuelve un cursor(*), no una lista ni un iterador
    else:
        nombre = nombre.capitalize()
        pokedex = db.samples_pokemon.find({ "$or": [{"name": {"$regex": nombre}}, {"type": {"$regex": nombre}}   ]})    # devuelve un cursor(*), no una lista ni un iterador
    
    lista_pokemon = []
    for pokemon in pokedex:
        lista_pokemon.append(pokemon)
        
    if len(lista_pokemon) >0 :
        return True
    else:
        return False



def busquedapokedexjson(nombre):
    if nombre.isdigit():
        pokedex = db.samples_pokemon.find({ "$or": [ {"id": float(nombre)}, {"num": float(nombre)}    ]})     # devuelve un cursor(*), no una lista ni un iterador
    else:
        nombre = nombre.capitalize()
        pokedex = db.samples_pokemon.find({ "$or": [{"name": {"$regex": nombre}}, {"type": {"$regex": nombre}}   ]})    # devuelve un cursor(*), no una lista ni un iterador
    
    lista_pokemon = []
    for pokemon in pokedex:
        lista_pokemon.append(pokemon)

    #lista_pokemon
    pokemon = {
            "name": lista_pokemon[0]["name"],
            "_id": str(lista_pokemon[0]["_id"]),
            "id": lista_pokemon[0]["id"],
            "num": lista_pokemon[0]["num"],
            
            "img": lista_pokemon[0]["img"],
            "type": lista_pokemon[0]["type"],
            "height": lista_pokemon[0]["height"],
            "weight": lista_pokemon[0]["weight"],
            "candy": lista_pokemon[0]["candy"],
            "egg": lista_pokemon[0]["egg"],
            "spawn_chance": lista_pokemon[0]["spawn_chance"],
            "avg_spawns": lista_pokemon[0]["avg_spawns"],
            "spawn_time": lista_pokemon[0]["spawn_time"],
            "multipliers": lista_pokemon[0]["multipliers"],
            "weaknesses": lista_pokemon[0]["weaknesses"],
                    
    
    }
    
    resp = jsonify(pokemon)
    resp.status_code = 200 # aquí cambiamos el código de estado a 400 (código muy común en caso de errores de solicitud)
    return resp
