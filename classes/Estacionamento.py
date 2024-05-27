# -*- coding: utf-8 -*-
"""
Created on Mon May 13 23:36:01 2024

@author: tiagoneves
"""

# Import the generic class
from classes.gclass import Gclass

from classes.Residente import Residente

class Estacionamento(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code', '_lugar','_matricula']
    # Class header title
    header = 'Estacionamento'
    # field description for use in, for example, in input form
    des = ['Código Residente','Nº de Lugar','Matrícula']
    # Constructor: Called when an object is instantiated
    def __init__(self,code, lugar,matricula):
        super().__init__()
        # Uncomment in case of auto number on
        if lugar == 'None':
            lugars = Estacionamento.getatlist('_lugar')
            if lugars == []:
                lugar = str(1)
            else:
                lugar = str(max(map(int,Estacionamento.getatlist('_lugar'))) + 1)
        
        # Object attributes
        
        # Check the customer referential integrity
        if code in Residente.lst:
            self._lugar = lugar
            self._matricula = matricula
            self._code = code
            # Add the new object to the Order list
            Estacionamento.obj[code] = self
            Estacionamento.lst.append(code)
        else:
            print('CodigoResidente ', code, ' not found')

       

    # Object properties
    # getter methodes
    # lugar property getter method
    @property
    def lugar(self):
        return self._lugar
    # matricula property getter method
    @property
    def matricula(self):
        return self._matricula
    # code property getter method
    @property
    def code(self):
        return self._code
    
    @lugar.setter
    def lugar(self, lugar):
        self._lugar = lugar
    
    # matricula property setter method
    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula
    # Code property setter method
    
    @code.setter
    def code(self, code):
        if code in Residente.lst:
            self._code = code
        else:
            print('CodigoResidente ', code, ' not found')