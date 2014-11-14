import requests
from requests.exceptions import ReadTimeout
import sys

from amara.bindery import html
import json

def dict_nodos():
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
	nodos = dict_nodos()
	up, down = estado_nodos(nodos)
	print
	print u"{} nodos OK: {}".format(len(up), u', '.join(up))
	print u"{} nodos DOWN: {}".format(len(down), u', '.join(down))

