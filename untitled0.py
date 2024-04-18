# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:40:19 2024

@author: braga
"""
from classes.order2Form import Order2Form   
from classes.customerorder import CustomerOrder

if __name__ == '__main__':
    
    clh = eval("Order2Form")
    
    clh.reset()
    diahoraselected = "2024-02-22"
    clh("None", CustomerOrder, diahoraselected)
    objh = clh.obj[clh.lst[0]]
    
    print (objh)
    print (objh.semanaTree)
    
    