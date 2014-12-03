# coding: utf-8

"""
Utilidades para subir archivos al servidor

"""


from fabric.operations import put
from fabric.contrib.project import rsync_project
from fabric.api import *
from fabric.contrib.files import exists
import os

env.user = 'luismigu'
env.hosts = ['proyectos.educa.aragon.es']


env.ruta = {
    'proyectos.educa.aragon.es': 'public_html/agrega/',
}


    

def sube_html():
    su = True
    destino = env.ruta.get(env.host)
#    if 'proyectos' in env.host:
#        su = False
    put("../agregas.html", destino+'index.html')
    


def sube_js():
    #ficheros = "mapa_centros_innova.html,centros_innova.js,proyectos_innova.js".split(',')
    # os.chdir('..')

    destino = env.ruta.get(env.host)
        
    put("../nodos.js", destino)
    put("../estado_nodos.js", destino)
    put("../agrega_aragon.csv", destino)

def subir():
	destino = env.ruta.get(env.host)
	if not exists(destino):
		sudo("mkdir " + destino)
	sube_html()
	sube_js() 	