# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:45:30 2024

@author: tiagoneves
"""

# Class Person - generic version with inheritance
from classes.gclass import Gclass
import datetime
class Residente(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0      # = 1 in case of auto number on
    nkey= 1
    # Attribute names list, identifier attribute must be the first one
    att = ['_code','_fname', '_lname','_email','_dob','_occupation']
    # Class header title
    header = 'Residente'
    # field description for use in, for example, input form
    des = ['ID Code','First Name','Last Name','Email Adress','Date of Birth','Occupation']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, fname, lname, email, dob, occupation):
        super().__init__()
        # Uncomment in case of auto number on
        # if code == 'None':
        #     codes = Person.getatlist('_code')
        #     if codes == []:
        #         code = str(1)
        #     else:
        #         code = str(max(map(int,Person.getatlist('_code'))) + 1)
        # Object attributes
        self._code = str(code)
        self._fname = fname
        self._lname = lname
        self._email = email
        self._dob = datetime.date.fromisoformat(dob)
        self._occupation = occupation
        # Add the new object to the dictionary of objects
        Residente.obj[code] = self
        # Add the code to the list of object codes
        Residente.lst.append(code)
    # code property getter method
    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, code):
        self._code = code
    # last name property getter method
    @property
    def fname(self):
        return self._fname
    @fname.setter
    def fname(self, fname):
        self._fname = fname
    # last name property getter method
    @property
    def lname(self):
        return self._lname
    @lname.setter
    def lname(self, lname):
        self._lname = lname
    #email property getter method
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email
    # dob property getter method
    
    @property
    def dob(self):
        return self._dob
    # dob property setter method
    @dob.setter
    def dob(self, dob):
        self._dob = dob
    # occupation property getter method
    @property
    def occupation(self):
        return self._occupation
    # occupation property setter method
    @occupation.setter
    def occupation(self, occupation):
        self._occupation = occupation
    # age property getter method
    @property
    def age(self):
        tday = datetime.date.today()
        age = tday.year - self.dob.year
        if tday.month < self.dob.month or \
            (tday.month == self.dob.month and tday.day < self.dob.day):
            age -= 1
        return age