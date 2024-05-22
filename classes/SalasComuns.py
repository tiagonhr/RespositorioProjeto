# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:14:43 2024

@author: tiagoneves
"""

#%% Class SalasComuns
# Import the generic class
from classes.gclass import Gclass

class SalasComuns(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0 # = 1 in case of auto number on
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_nome','_foto']
    # Class header title
    header = 'Salas Comuns'
    # field description for use in, for example, in input form
    des = ['Codigo','Tipo','Foto']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, nome, foto):
        super().__init__()
        # Uncomment in case of auto number on
        # if code == 'None':
        #     codes = SalasComuns.getatlist('_code')
        #     if codes == []:
        #         code = str(1)
        #     else:
        #         code = str(max(map(int,SalasComuns.getatlist('_code'))) + 1)
        # Object attributes
        self._code = code
        self._nome = nome
        self._foto = foto
        # Add the new object to the SalasComuns list
        SalasComuns.obj[code] = self
        SalasComuns.lst.append(code)
    # Object properties
    # code property getter method
    @property
    def code(self):
        return self._code
    # nome property getter method
    @property
    def nome(self):
        return self._nome
    @property
    def foto(self):
        return self._foto
    @foto.setter
    def foto(self, foto):
        self._foto = foto