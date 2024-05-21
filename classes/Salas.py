# -*- coding: utf-8 -*-
"""
Created on Tue May 14 02:57:13 2024

@author: tiagoneves
"""

#%% Class Salas
# Import the generic class
from classes.gclass import Gclass

class Salas(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0 # = 1 in case of auto number on
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_NomeSala']
    # Class header title
    header = 'Salas para Alugar'
    # field description for use in, for example, in input form
    des = ['NomeSala']
    # Constructor: Called when an object is instantiated
    def __init__(self, NomeSala):
        super().__init__()
        # Uncomment in case of auto number on
        # if NomeSala == 'None':
        #     NomeSalas = Salas.getatlist('_NomeSala')
        #     if NomeSalas == []:
        #         NomeSala = str(1)
        #     else:
        #         NomeSala = str(max(map(int,Salas.getatlist('_NomeSala'))) + 1)
        # Object attributes
        self._NomeSala = NomeSala
        # Add the new object to the Salas list
        Salas.obj[NomeSala] = self
        Salas.lst.append(NomeSala)
    # Object properties
    # NomeSala property getter method
    @property
    def NomeSala(self):
        return self._NomeSala
