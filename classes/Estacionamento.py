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
    auto_number = 1
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_lugar','_matricula','_CodigoResidente']
    # Class header title
    header = 'Estacionamento'
    # field description for use in, for example, in input form
    des = ['Lugar número','matricula do Veiculo','Codigo do Residente']
    # Constructor: Called when an object is instantiated
    def __init__(self, lugar,matricula,CodigoResidente):
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
        if CodigoResidente in Residente.lst:
            self._lugar = lugar
            self._matricula = matricula
            self._CodigoResidente = CodigoResidente
            # Add the new object to the Order list
            Estacionamento.obj[lugar] = self
            Estacionamento.lst.append(lugar)
        else:
            print('CodigoResidente ', CodigoResidente, ' not found')

       

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
    # CodigoResidente property getter method
    @property
    def CodigoResidente(self):
        return self._CodigoResidente
    
    @lugar.setter
    def lugar(self, lugar):
        self._lugar = lugar
    
    # matricula property setter method
    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula
    # CodigoResidente property setter method
    @CodigoResidente.setter
    def CodigoResidente(self, CodigoResidente):
        if CodigoResidente in Residente.lst:
            self._CodigoResidente = CodigoResidente
        else:
            print('CodigoResidente ', CodigoResidente, ' not found')