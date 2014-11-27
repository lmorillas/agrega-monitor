#!/usr/bin/env python
from monitoring import *
__doc__ = """
Queries the Google search engin and fail if the query takes
more than 80ms.
"""
Monitor(
	Service(
		name='agrega',
		monitor = (
			HTTP(
				GET="http://agrega.juntadeandalucia.es/",
				freq=Time.s(1),
				timeout=Time.ms(5000),
				fail=[
					Print("Agrega Esta petao")
				],
				success=[
					Print("Agrega esta OK")
				]
			)
		)
	)
).run(iterations=1)


