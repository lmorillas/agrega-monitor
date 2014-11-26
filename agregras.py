import requests
from requests.exceptions import ReadTimeout
import sys


import json

def dict_nodos():
	'''
	Extrae nodos de la web de agrega2
	'''
	from amara.bindery import html
	doc = html.parse('http://www.agrega2.es/web/')
	doc.xml_select(u'//div[@id="block-views-nodos-de-agrega-block-1"]//li//a')
	nodos = doc.xml_select(u'//div[@id="block-views-nodos-de-agrega-block-1"]//li//a')
	nodos_agrega = dict([(unicode(n), n.href) for n in nodos])
	return nodos_agrega

def conecta(n, t=None):
	try:
		r = requests.get(n, timeout=t)
		if r.status_code == 200:
			return True
		else:
			return False
	except ReadTimeout:
		return False


def estado_nodos(nodos_agrega):
	up = []
	down = []
	for n in nodos_agrega:
		if conecta(nodos_agrega.get(n), 2):
			print >> sys.stderr, '.',
			up.append(n)
		else:
			down.append(n)
			print >> sys.stderr,  'x',
	print
	return up, down

if __name__ == '__main__':
	# nodos = dict_nodos()
	{u'Andaluc\xeda': u'http://agrega.juntadeandalucia.es',
 u'Arag\xf3n': u'http://agrega.catedu.es/',
 u'Baleares': u'http://agrega.caib.es',
 u'Canarias': u'http://www3.gobiernodecanarias.org/medusa/agrega',
 u'Cantabria': u'http://agrega.educantabria.es',
 u'Castilla y Le\xf3n': u'http://agrega.crfptic.es/',
 u'Castilla-La Mancha': u'http://agrega.educa.jccm.es',
 u'Extremadura': u'http://agrega.educarex.es',
 u'Galicia': u'http://www.edu.xunta.es/agrega',
 u'INTEF': u'http://agrega.educacion.es',
 u'La Rioja': u'http://agrega.educarioja.org',
 u'Madrid': u'http://agrega.educa.madrid.org',
 u'Murcia': u'http://agrega.carm.es',
 u'Navarra': u'http://agrega.educacion.navarra.es',
 u'Pa\xeds Vasco': u'http://agrega.hezkuntza.net',
 u'Valencia': u'http://recursos.edu.gva.es'}



	nodos = {u'Canarias': u'http://www3.gobiernodecanarias.org/medusa/agrega', u'Castilla y Le\xf3n': u'http://agrega.crfptic.es/', u'Andaluc\xeda': u'http://agrega.juntadeandalucia.es', u'Arag\xf3n': u'http://agrega.catedu.es/', u'Madrid': u'http://agrega.educa.madrid.org', u'Murcia': u'http://agrega.carm.es', u'Pa\xeds Vasco': u'http://agrega.hezkuntza.net', u'Baleares': u'http://agrega.caib.es', u'La Rioja': u'http://agrega.educarioja.org', u'Castilla-La Mancha': u'http://agrega.educa.jccm.es', u'Galicia': u'http://www.edu.xunta.es/agrega', u'Cantabria': u'http://agrega.educantabria.es', u'Valencia': u'http://recursos.edu.gva.es', u'INTEF': u'http://agrega.educacion.es', u'Extremadura': u'http://agrega.educarex.es', u'Navarra': u'http://agrega.educacion.navarra.es'}
	pprint(nodos)
	up, down = estado_nodos(nodos)
	print
	print u"{} nodos OK: {}".format(len(up), u', '.join(up))
	print u"{} nodos DOWN: {}".format(len(down), u', '.join(down))

