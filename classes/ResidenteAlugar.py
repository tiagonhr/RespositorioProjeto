# -*- coding: utf-8 -*-
"""
Created on Tue May 14 03:09:10 2024

@author: tiagoneves
"""

#%% Class Alugar
import datetime
from classes.Residente import Residente
# Import the generic class
from classes.gclass import Gclass

class ResidenteAlugar(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0 # = 1 in case of auto number on
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_sala','_date','_CodigoResidente']
    # Class header title
    header = 'Alugar'
    # field description for use in, for example, in input form
    des = ['sala','Date','Residente sala']
    # Constructor: Called when an object is instantiated
    def __init__(self, sala, date, CodigoResidente):
        super().__init__()
        # Uncomment in case of auto number on
        # if sala == 'None':
        #     salas = ResidenteAlugar.getatlist('_sala')
        #     if salas == []:
        #         sala = str(1)
        #     else:
        #         sala = str(max(map(int,ResidenteAlugar.getatlist('_sala'))) + 1)
        # Object attributes
        # Check the Residente referential integrity
        if CodigoResidente in Residente.lst:
            self._sala = sala
            self._date = datetime.date.fromisoformat(date)
            self._CodigoResidente = CodigoResidente
            # Add the new object to the Alugar list
            ResidenteAlugar.obj[sala] = self
            ResidenteAlugar.lst.append(sala)
        else:
            print('Residente ', CodigoResidente, ' not found')
    # Object properties
    # sala property getter method
    @property
    def sala(self):
        return self._sala
    # date property getter method
    @property
    def date(self):
        return self._date
    # date property setter method
    @date.setter
    def date(self, date):
        self._date = date
    # Residente property getter method
    @property
    def CodigoResidente(self):
        return self._CodigoResidente
    # Residente property setter method
    @CodigoResidente.setter
    def CodigoResidente(self, CodigoResidente):
        if CodigoResidente in Residente.lst:
            self._CodigoResidente = CodigoResidente
        else:
            print('Residente ', CodigoResidente, ' not found')