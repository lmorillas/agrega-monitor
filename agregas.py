import requests
import json
import sys

def extrae_nodos():
    from amara.bindery import html
    doc = html.parse('http://www.agrega2.es/web/')
    doc.xml_select(u'//div[@id="block-views-nodos-de-agrega-block-1"]//li//a')

    nodos = doc.xml_select(u'//div[@id="block-views-nodos-de-agrega-block-1"]//li//a')

    nodos_agrega = dict([(unicode(n), n.href) for n in nodos])
    return nodos_agrega


nodos_agrega = {u'Canarias': u'http://www3.gobiernodecanarias.org/medusa/agrega', u'Castilla y Le\xf3n': u'http://agrega.crfptic.es/', u'Andaluc\xeda': u'http://agrega.juntadeandalucia.es', u'Arag\xf3n': u'http://agrega.catedu.es/', u'Madrid': u'http://agrega.educa.madrid.org', u'Murcia': u'http://agrega.carm.es', u'Pa\xeds Vasco': u'http://agrega.hezkuntza.net', u'Baleares': u'http://agrega.caib.es', u'La Rioja': u'http://agrega.educarioja.org', u'Castilla-La Mancha': u'http://agrega.educa.jccm.es', u'Galicia': u'http://www.edu.xunta.es/agrega', u'Cantabria': u'http://agrega.educantabria.es', u'Valencia': u'http://recursos.edu.gva.es', u'INTEF': u'http://agrega.educacion.es', u'Extremadura': u'http://agrega.educarex.es', u'Navarra': u'http://agrega.educacion.navarra.es'}



estado_nodos = []
estado_aragon = ''

for n in nodos_agrega:
    nodo ={'label':n,
    'type': 'estado'}
    try:
        r = requests.get(nodos_agrega.get(n), timeout=1)
        if r.status_code == 200:
            #print n, '--> OK'
            #print >> sys.stderr, '.',
            nodo['estado'] = 'on'
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

json.dump({'items':estado_nodos}, open('estado_nodos.js', 'w'), indent=True)

import csv
from datetime import datetime

with open('agrega_aragon.csv', 'a') as fp:
	fw = csv.writer(fp, delimiter=',')
	fw.writerow([datetime.now().isoformat(), estado_aragon, 'ar' ])