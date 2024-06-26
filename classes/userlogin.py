# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2022)
#objective: class Person
"""""
#%% Class User - generic version
# import sys
import bcrypt
# Import the generic class
from classes.gclass import Gclass

class Userlogin(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code', '_user','_usergroup','_password']
    # Class header title
    header = 'Utilizadores'
    # field description for use in, for example, in input form
    des = ['Código Utilizador','Utilizador','Grupo','Password']
    username = ''
    # Constructor: Called when an object is instantiated
    def __init__(self,code , user, usergroup, password):
        super().__init__()
        # Uncomment in case of auto number on
        if code == 'None':
            code = Userlogin.getatlist('_code')
            if code == []:
                code = str(1)
            else:
                code = str(max(map(int,Userlogin.getatlist('_code'))) + 1)
        # Object attributes
        self._user = user
        self._usergroup = usergroup
        self._password = password
        self._code = code
        # Add the new object to the dictionary of objects
        Userlogin.obj[user] = self
        # Add the code to the list of object codes
        Userlogin.lst.append(user)

    # code property getter method
    @property
    def user(self):
        return self._user
    # name property getter method
    @property
    def usergroup(self):
        return self._usergroup
    @usergroup.setter
    def usergroup(self, usergroup):
        self._usergroup = usergroup
        
    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, code):
        self._code = code
    @usergroup.setter
    def usergroup(self, code):
        self._code = code      
        
    @property
    def password(self):
        return ""
    
    @password.setter
    def password(self, password):
        self._password = password

    @classmethod
    def chk_password(self, user, password):
        if user in Userlogin.obj:
            obj = Userlogin.obj[user]
            valid = bcrypt.checkpw(password.encode(), obj._password.encode())
            message = "Valid"
            if not valid:
                message = 'Wrong password'
        else:
            message = 'No existent user'
        return message
    @classmethod
    def set_password(self, password):
        passencrypted = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return passencrypted.decode()
    
    
