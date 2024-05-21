# -*- coding: utf-8 -*-
"""
Created on Mon May 13 03:12:14 2024

@author: tiagoneves
"""
# Import the generic class
from classes.gclass import Gclass

from classes.Residente import Residente

class Reserva(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_numero','_tipologia','_CodigoResidente']
    # Class header title
    header = 'Reserva'
    # field description for use in, for example, in input form
    des = ['Número do Quarto','Tipologia do Quarto','Codigo do Residente']
    # Constructor: Called when an object is instantiated
    def __init__(self, numero,tipologia,CodigoResidente):
        super().__init__()
        # Uncomment in case of auto number on
        # if numero == 'None':
        #     numeros = Reserva.getatlist('_numero')
        #     if numeros == []:
        #         numero = str(1)
        #     else:
        #         numero = str(max(map(int,Reserva.getatlist('_numero'))) + 1)
        
        # Object attributes
        
        # Check the customer referential integrity
        if CodigoResidente in Residente.lst:
            self._numero = numero
            self._tipologia = tipologia
            self._CodigoResidente = CodigoResidente
            # Add the new object to the Order list
            Reserva.obj[numero] = self
            Reserva.lst.append(numero)
        else:
            print('CodigoResidente ', CodigoResidente, ' not found')

       

    # Object properties
    # getter methodes
    # numero property getter method
    @property
    def numero(self):
        return self._numero
    # tipologia property getter method
    @property
    def tipologia(self):
        return self._tipologia
    # CodigoResidente property getter method
    @property
    def CodigoResidente(self):
        return self._CodigoResidente
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero
    
    # tipologia property setter method
    @tipologia.setter
    def tipologia(self, tipologia):
        self._tipologia = tipologia
    # CodigoResidente property setter method
    @CodigoResidente.setter
    def CodigoResidente(self, CodigoResidente):
        if CodigoResidente in Residente.lst:
            self._CodigoResidente = CodigoResidente
        else:
            print('CodigoResidente ', CodigoResidente, ' not found')    