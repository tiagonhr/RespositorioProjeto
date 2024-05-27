# Import the generic class
from classes.gclass import Gclass
from classes.ReservaGinasio import ReservaGinasio

class InscricaoGinasio(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code_aula','_nome','_code']
    # Class header title
    header = 'InscricaoGinasio'
    # field description for use in, for example, in input form
    des = ['Código da Aula','Nome Inscrição','Código Residente']
    # Constructor: Called when an object is instantiated
    def __init__(self, code_aula,nome,code):
        super().__init__()
        # Uncomment in case of auto number on
        # if code_aula == 'None':
        #     code_aulas = InscricaoGinasio.getatlist('_code_aula')
        #     if code_aulas == []:
        #         code_aula = str(1)
        #     else:
        #         code_aula = str(max(map(int,InscricaoGinasio.getatlist('_code_aula'))) + 1)
        if code_aula in ReservaGinasio.lst:
            self._code_aula = code_aula
            self._nome = nome
            # self._nome = nometime.nome.fromisoformat(nome)
            self._code = code
            # Add the new object to the Order list
            InscricaoGinasio.obj[code_aula] = self
            InscricaoGinasio.lst.append(code_aula)
        else:
            raise ValueError(f'Erro: ReservaGinasio {code_aula} não está na lista de aulas')

       

    # Object properties
    # getter methodes
    # code_aula property getter method
    @property
    def code_aula(self):
        return self._code_aula
    # nome property getter method
    @property
    def nome(self):
        return self._nome
    # aula property getter method
    @property
    def aula(self):
        return self._code
    
    # nome property setter method
    @nome.setter
    def nome(self, nome):
        self._nome = nome