# -*- coding: utf-8 -*-
"""
Created on Sat May 11 21:28:06 2024

@author: tiagoneves
"""

from datafile import filename

from classes.Residente import Residente

Residente.read(filename + 'Residencia.db')

obj = Residente.from_string("222;a;b;c;2005-09-30;e")

print("objeto sem estar gravado ",obj)

Residente.insert(getattr(obj,Residente.att[0]))

obj = Residente.from_string("333;f;g;h;2004-08-29;j")
Residente.insert(getattr(obj,Residente.att[0]))


print("\nLista dos onjetos gravados " ,Residente.lst)

obj = Residente.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.fname = "ola"
Residente.update(getattr(obj, Residente.att[0]))

Residente.read(filename + 'Residencia.db')

print("\nobjectos gravados")    
for code in Residente.lst:
    print(Residente.obj[code])