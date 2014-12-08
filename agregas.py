#!/usr/bin/env python
# coding: utf-8

import requests
import json
import sys
from random import choice
import os

# por defecto los archivos estarán en el mismo directorio
RUTA = os.path.dirname(os.path.abspath(__file__))+'/'

def extrae_nodos():
    from amara.bindery import html
    doc = html.parse('http://www.agrega2.es/web/')
    doc.xml_select(u'//div[@id="block-views-nodos-de-agrega-block-1"]//li//a')

    nodos = doc.xml_select(u'//div[@id="block-views-nodos-de-agrega-block-1"]//li//a')

    nodos_agrega = dict([(unicode(n), n.href) for n in nodos])
    return nodos_agrega


nodos_agrega = {u'Canarias': u'http://www3.gobiernodecanarias.org/medusa/agrega',
    u'Castilla y Le\xf3n': u'http://agrega.crfptic.es/',
    u'Andaluc\xeda': u'http://agrega.juntadeandalucia.es',
    u'Arag\xf3n': u'http://agrega.catedu.es/', u'Madrid': u'http://agrega.educa.madrid.org' ,
    u'Murcia': u'http://agrega.carm.es', u'Pa\xeds Vasco': u'http://agrega.hezkuntza.net',
    u'Baleares': u'http://agrega.caib.es', u'La Rioja': u'http://agrega.educarioja.org',
    u'Castilla-La Mancha': u'http://agrega.educa.jccm.es',
    u'Galicia': u'http://www.edu.xunta.es/agrega',
    u'Cantabria': u'http://agrega.educantabria.es', u'Valencia': u'http://recursos.edu.gva.es',
    u'INTEF': u'http://agrega.educacion.es', u'Extremadura': u'http://agrega.educarex.es',
    u'Navarra': u'http://agrega.educacion.navarra.es'}



estado_nodos = []
estado_aragon = ''

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0)  Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'
    ]


headers = {
    "User-Agent" : choice(USER_AGENT_LIST) }

for n in nodos_agrega:
    nodo ={'label':n,
    'type': 'estado'}
    try:
        r = requests.get(nodos_agrega.get(n), headers=headers, timeout=5)
        if r.status_code == 200:
            #print n, '--> OK'
            #print >> sys.stderr, '.',
            nodo['estado'] = 'on'
            estado_nodos.append(nodo)
        else:
            nodo['estado'] = 'off'
            estado_nodos.append(nodo)
    except:
        #print n, '--> DOWN :-('
        nodo['estado'] = 'off'
        estado_nodos.append(nodo)
        #print >> sys.stderr, 'x',
    if n == u'Arag\xf3n':
    	estado_aragon = nodo['estado']


'''
print
print u"{} nodos OK: {}".format(len(up), u', '.join(up))
print u"{} nodos DOWN: {}".format(len(down), u', '.join(down))
'''

json.dump({'items':estado_nodos}, open(RUTA + 'estado_nodos.js', 'w'), indent=True)

import csv
from datetime import datetime

ahora = datetime.now()

def pon_hora(ahorat):
    texto_hora = '<h2 id="fecha">Estado nodos Agrega :: '
    ahora = ahorat.strftime("%d-%b-%y %H:%M")
    open(RUTA + 'index.html', 'w').write(open(RUTA + 'agregas.html').read().replace(texto_hora, texto_hora + ahora))

pon_hora(ahora)

with open(RUTA + 'agrega_aragon.csv', 'a') as fp:
	fw = csv.writer(fp, delimiter=',')
	fw.writerow([ahora.isoformat(), estado_aragon, 'ar' ])
