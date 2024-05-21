# -*- coding: utf-8 -*-
"""
Created on Mon May 13 03:32:08 2024

@author: tiagoneves
"""

from datafile import filename

from classes.Residente import Residente
from classes.Reserva import Reserva


Residente.read(filename + 'Residencia.db')
Reserva.read(filename + 'Residencia.db')

cname = "Reserva"
cl = eval(cname)

obj = cl.from_string("504;Studio;1")

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

obj = cl.from_string("560;Studio;333")

cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos onjetos gravados " ,cl.lst)


# alterar
obj = cl.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.tipologia = "Duplo"
Residente.update(getattr(obj, cl.att[0]))

cl.read(filename + 'Residencia.db')

print("\nobjectos gravados")    
for numero in cl.lst:
    print(cl.obj[numero])