# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:04:56 2024

@author: tiagoneves
"""

from datetime import datetime

from datetime import timedelta
from classes.gclass import Gclass



class Alugar2Form(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    
    att = ['code','classEvents', 'selectedDiaHora']
    header = 'horario to form'
    des = ['code','classEvents', 'selectedDiaHora']
    def __init__(self, code,classEvents, selectedDiaHora):
        #Uncomment in case of auto number on
        # if code == 'None':
        #     codes = Alugar2Form.getatlist('_code')
        #     if codes == []:
        #         code = str(1)
        #     else:
        #         code = str(max(map(int,Alugar2Form.getatlist('_code'))) + 1)
        # Object attributes
        self.code = code
        self.classEvents = classEvents
        

        self.selectedDiaHora = Alugar2Form.str2datetimeDiaHora(selectedDiaHora)

        self._eventsdiahseleted = []
        
        self.config_horario()
        self.fillMatiz()

        Alugar2Form.obj[code] = self
        Alugar2Form.lst.append(code)
#%% properties

    @property
    def code(self):
        return self._code

    @property
    def classEvents(self):
        return self._classEvents
   
    @property
    def selectedDia(self):
        return self.selectedDiaHora.date()
    
    @property
    def eventsdiahseleted(self):
        return self._eventsdiahseleted
    

#%% setter
    
    @code.setter
    def code(self, code):
        self._code = code

    @classEvents.setter
    def classEvents(self, classEvents):
        self._classEvents = classEvents

#%% def    


           
       
    def str2datetimeDiaHora(datestr):
        
        if type (datestr) == str:
            datestr = datestr.replace("/", ";")
            datestr = datestr.replace("-", ";")
            datestr = datestr.replace(":", ";")
            datestr = datestr.replace(" ", ";")
            
            
            
            try:
                
                diahorastr =list(map(int, datestr.split(";")))
                
                 
                date = datetime(diahorastr[0], diahorastr[1], diahorastr[2])
                if len(diahorastr)>3:
                    date=date.replace(hour = diahorastr[3])
                if len(diahorastr)>4:
                    date=date.replace(minute=  diahorastr[4])
                if len(diahorastr)>5:
                    date=date.replace(second = diahorastr[5])
            except:
                date = datetime.now()
                

        else:
            date = datestr
        if type(date) == datetime:
            date = datetime(date.year, date.month, date.day,date.hour)
            
        else:
             date = datetime(date.year, date.month, date.day)
        return date
    

    def config_horario(self):
        #dia a mostrar  no horario
        # self.selectedDia
        
    
        #calcular o 1º e ultimo dia da semana que contem o dia
        self.diaInicial = self.selectedDia+timedelta(days=-int(self.selectedDia.strftime("%w")))
        self.diaFinal = self.diaInicial+timedelta(days=+6)
        
        self.colunas=('D','2ª','3ª','4ª','5ª','6ª','S')
        self.colunasdia = list()
        for k in range(7):
            self.colunasdia.append(self.diaInicial+ timedelta(k))
            
             
    def fillMatiz(self):
        
          
        self.semanaTree = []

        self.clientes = []
        
        
                
        l=0
 
        for k in self.classEvents.lst:
            evento = self.classEvents.obj[k]
            
            diaEvento = evento.date
            if diaEvento >= self.diaInicial and diaEvento <= self.diaFinal:
                
                c=int(diaEvento.strftime("%w"))

                
                self.clientes.append(evento.customer_code)

                self.linha = [""]*7
                
                dia = diaEvento
                self.linha[c] = celulaform(l,c,dia,l)
                self.linha[c].codeevent = evento.customer_code 
                self.linha[c].texto = self.text_to_horario(evento)
                self.semanaTree.append(self.linha)
          
        

      
    def text_to_horario(self,evento):
        texto = f"{evento._customer_code} - {evento.date} - {evento.room_code} "
       
        return texto
       
    
 
        
        
                
class celulaform():
    def __init__(self,l,c,dia,hora):
        self.cores = {
            0: 'White',
            1: 'GreenYellow',
            2: 'OrangeRed',
            3: 'red'}
        
        self.nevents = -1
        self.l = l
        self.c = c
        self.dia = dia
        self.hora =hora
        self.codeevent = "None"
        self.texto = "" 
        
    @property
    def codeevent(self):
        return self._codeevent
    
    @property
    def cor(self):
        if self.nevents in self.cores.keys():
            temp = self.cores[self.nevents]
        else:
            temp = self.cores[len(self.cores)-1]
        
        return temp
  
    @codeevent.setter
    def codeevent(self, codeevent):
        self.nevents += 1
        self._codeevent = codeevent
    
    def __str__(self):
        return f'{self.l} -{self.c} -{self.dia} -{self.hora} -{self.codeevent} -{self.texto} - '