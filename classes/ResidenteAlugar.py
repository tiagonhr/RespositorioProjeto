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
    att = ['_customer_code','_date','_room_code']
    # Class header title
    header = 'Alugar'
    # field description for use in, for example, in input form
    des = ['Código Residente','Date','Código Sala']
    # Constructor: Called when an object is instantiated
    def __init__(self, customer_code, date, room_code):
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
        if room_code in Residente.lst:
            self._customer_code = customer_code
            self._date = datetime.date.fromisoformat(date)
            self._room_code = room_code
            # Add the new object to the Alugar list
            ResidenteAlugar.obj[customer_code] = self
            ResidenteAlugar.lst.append(customer_code)
        else:
            print('Residente ', customer_code, ' not found')
    # Object properties
    # code property getter method
    @property
    def room_code(self):
        return self._room_code
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