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

def gformT(cname='', submenu="", grupo="", code=""):
    global prev_option

    ulogin = session.get("user")
    if ulogin != None:
        print(cname)
        sbl = eval(cname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        
       
        obj = sbl.obj.get(code)

        if prev_option == 'edit' and option == 'save':
            # Handle edit and save logic
            print("prev_option == 'edit' and option == 'save':")
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            
            elif option == 'cancel':
                pass
            
            elif option == "saverow":
                if sbl.auto_number == 1:
                    strobj = "None"
                else:
                    strobj = request.form[sbl.att[0]]
                for i in range(1, len(sbl.att)):
                    strobj += ";" + request.form[sbl.att[i]]
                print(strobj)
                objl = sbl.from_string(strobj)
                code = str(getattr(objl, sbl.att[0]))
                sbl.insert(code)
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"))
        
        prev_option = option

        headers = [sbl.att[i][1:] for i in range(1, len(sbl.att))]
        objl = [sbl.obj[line] for line in sbl.lst]

        return render_template(
            "gformTusers.html",
            butshow=butshow,
            butedit=butedit,
            cname=cname,
            ulogin=session.get("user"),
            objl=objl,
            headerl=sbl.header,
            desl=sbl.des,
            attl=sbl.att,
            submenu=submenu
        )
    else:
        return render_template("index.html", ulogin=ulogin)
