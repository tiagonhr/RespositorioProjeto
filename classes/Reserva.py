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
    att = ['_code','_numero','_tipologia']
    # Class header title
    header = 'Reserva'
    # field description for use in, for example, in input form
    des = ['Código Residente', 'Número do Quarto','Tipologia do Quarto']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, numero,tipologia):
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
        if code in Residente.lst:
            self._numero = numero
            self._tipologia = tipologia
            self._code = code
            # Add the new object to the Order list
            Reserva.obj[code] = self
            Reserva.lst.append(code)
        else:
            print('code ', code, ' not found')

       

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
    # code property getter method
    @property
    def code(self):
        return self._code
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero
    
    # tipologia property setter method
    @tipologia.setter
    def tipologia(self, tipologia):
        self._tipologia = tipologia
    # code property setter method
    @code.setter
    def code(self, code):
        if code in Residente.lst:
            self._code = code
        else:
            print('code ', code, ' not found')    
            
