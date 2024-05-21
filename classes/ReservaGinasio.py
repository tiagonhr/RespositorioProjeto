# -*- coding: utf-8 -*-
"""
Created on Tue May 21 09:00:05 2024

@author: tiagoneves
"""

#%% Class ReservaGinasio
# Import the generic class
from classes.gclass import Gclass

class ReservaGinasio(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0 # = 1 in case of auto number on
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_name','_aula', '_foto']
    # Class header title
    header = 'ReservaGinasios'
    # field description for use in, for example, in input form
    des = ['Codigo','Nome','aula','Foto']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, name, aula,foto):
        super().__init__()
        # Uncomment in case of auto number on
        # if code == 'None':
        #     codes = ReservaGinasio.getatlist('_code')
        #     if codes == []:
        #         code = str(1)
        #     else:
        #         code = str(max(map(int,ReservaGinasio.getatlist('_code'))) + 1)
        # Object attributes
        self._code = code
        self._name = name
        self._aula = aula
        self._foto = foto
        # Add the new object to the ReservaGinasio list
        ReservaGinasio.obj[code] = self
        ReservaGinasio.lst.append(code)
    # Object properties
    # code property getter method
    @property
    def code(self):
        return self._code
    # name property getter method
    @property
    def name(self):
        return self._name
    # aula property getter method
    @property
    def aula(self):
        return self._aula
    @property
    def foto(self):
        return self._foto
    # aula property setter method
    @aula.setter
    def aula(self, aula):
        self._aula = aula
    # foto property setter method
    @foto.setter
    def foto(self, foto):
        self._foto = foto
