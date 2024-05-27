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
    att = ['_code','_date','_customer_code']
    # Class header title
    header = 'Alugar'
    # field description for use in, for example, in input form
    des = ['Código da Sala','Date','Código Residente']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, date, customer_code):
        super().__init__()
        # Uncomment in case of auto number on
        # if code == 'None':
        #     codes = ResidenteAlugar.getatlist('_code')
        #     if codes == []:
        #         code = str(1)
        #     else:
        #         code = str(max(map(int,ResidenteAlugar.getatlist('_code'))) + 1)
        # Object attributes
        # Check the Residente referential integrity
        if customer_code in Residente.lst:
            self._code = code
            self._date = datetime.date.fromisoformat(date)
            self._customer_code = customer_code
            # Add the new object to the Alugar list
            ResidenteAlugar.obj[code] = self
            ResidenteAlugar.lst.append(code)
        else:
            print('Residente ', customer_code, ' not found')
    # Object properties
    # code property getter method
    @property
    def code(self):
        return self._code
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
    def customer_code(self):
        return self._customer_code
    # Residente property setter method
    @customer_code.setter
    def customer_code(self, customer_code):
        if customer_code in Residente.lst:
            self._customer_code = customer_code
        else:
            print('Residente ', customer_code, ' not found')