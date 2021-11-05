

from pickleshare import *

db = PickleShareDB('miBD')

def escribirbd(nombre,psw):
    
    db[nombre] = {'psw':psw}
    return db[nombre]

def leerbd(nombre):
    return db[nombre]['psw']

def exiteuser(nombre):
    if nombre in db:
        return True
    else:
        return False