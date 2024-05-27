# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: subs_gformT.py

"""""
from flask import Flask, render_template, request, session
from classes.Residente import Residente
from classes.Reserva import Reserva
from classes.Estacionamento import Estacionamento
from classes.ResidenteAlugar import ResidenteAlugar
from classes.ReservaGinasio import ReservaGinasio
from classes.InscricaoGinasio import InscricaoGinasio
from classes.SalasComuns import SalasComuns


from classes.customer import Customer
from classes.product import Product
from classes.customerorder import CustomerOrder
from classes.orderproduct import OrderProduct
from classes.userlogin import Userlogin

prev_option = ""

def gformT(cname='',submenu="",grupo="",code=""):
    global prev_option
    
    scname = eval(cname)
    ulogin=session.get("user")
    if (grupo != None):
        print(cname)
        cl = eval(cname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if prev_option == 'insert' and option == 'save':
            if (cl.auto_number == 1):
                strobj = "None"
            else:
                strobj = request.form[cl.att[0]]
            for i in range(1,len(cl.att)):
                strobj += ";" + request.form[cl.att[i]]
            obj = cl.from_string(strobj)
            cl.insert(getattr(obj, cl.att[0]))
            cl.last()
            print("prev_option == 'insert' and option == 'save':")
        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            # if auto_number = 1 the key stays the same
            for i in range(cl.auto_number,len(cl.att)):
                att = cl.att[i]
                setattr(obj, att, request.form[att])
            cl.update(getattr(obj, cl.att[0]))
            print("prev_option == 'edit' and option == 'save':")
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "delete":
                obj = cl.current()
                lines = cl.getlines(getattr(obj, cl.att[0]))
                for line in lines:
                    cl.remove(line)
                cl.remove(obj.code)
                if not cl.previous():
                    cl.first()
                print('option == "delete":')
            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"
            elif option == 'cancel':
                pass
            elif option == "first":
                #cl.first()
                print('option == "first":')
            elif option == "previous":
                #cl.previous()
                print('option == "previous":')
            elif option == "next":
                #cl.nextrec()
                print('option == "next":')
            elif option == "last":
                #cl.last()
                print('option == "last":')
            elif option[:6] == "delrow":
                row = int(option.split("_")[1])
                # obj = cl.current()
                # lines = cl.getlines(getattr(obj, cl.att[0]))
                # print(row,lines[row])
                # cl.remove(lines[row])
                
               
                cl.remove(cl.lst[row])
                if not cl.previous():
                    cl.first()
                
            elif option == "addrow":
                butshow = "disabled"
                butedit = "disabled"
            elif option == "saverow":
               
                if (cl.auto_number == 1):
                    strobj = "None"
                else:
                    strobj = request.form[cl.att[0]]
                for i in range(1,len(cl.att)):
                    strobj += ";" + request.form[cl.att[i]]
                print (strobj)
                objl = cl.from_string(strobj)
                #code = str(getattr(objl, cl.att[0])) + str(getattr(objl, cl.att[1]))
                code = str(getattr(objl, cl.att[0]))
                cl.insert(code)
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user")) 
        prev_option = option
        # obj = cl.current()
        # headers = list()
        # objl = list()
        # if option == 'insert' or len(cl.lst) == 0:
        #     obj = dict()
        #     for att in cl.att:
        #         obj[att] = ""
        # else:
        #     for i in range(1, len(cl.att)): 
        #             headers.append(cl.att[i][1:])        
        #     lines = cl.getlines(getattr(obj, cl.att[0])) 
        #     for line in lines:
        #         objl.append(cl.obj[line])
        
        
        headers = list()
        
        for i in range(1, len(cl.att)): 
                headers.append(cl.att[i][1:])        
        objl = list()
        for line in cl.lst:
            objl.append(cl.obj[line])
        # return render_template("subform.html", butshow=butshow, butedit=butedit,
        #             cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
        #             ulogin=session.get("user"),objl=objl,headerl=cl.header,
        #             desl=cl.des, attl=cl.att, auto_number=cl.auto_number)
        return render_template("gformT.html", butshow=butshow, butedit=butedit,
                    cname=cname, 
                    ulogin=session.get("user"),objl=objl,headerl=cl.header,
                    desl=cl.des, attl=cl.att,
                    submenu=submenu)
    else:
        return render_template("index.html", ulogin=ulogin)

