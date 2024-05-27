# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: subs_gform.py

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

from classes.gclass import Gclass
prev_option = ""




def gform(cname='', submenu="", grupo="",code = ""):
    global prev_option
    ulogin = session.get("user")
    cl = eval(cname)
    if  ulogin != None:
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        obj = cl.obj.get(code)  # Get the specific object using the provided code
        
        if obj is None:
           if prev_option == 'insert' and option == 'save':  # Verifica se a opção anterior era inserir e a atual é salvar
                if cl.auto_number == 1:
                    code = "None"  # Define o código como None se for auto numerado
                else:
                    code = request.form[cl.att[0]]  # Obtém o valor do formulário para o primeiro atributo (código)

                # Cria um dicionário com os valores do formulário
                form_data = {att: request.form[att] for att in cl.att}

                # Cria um novo objeto usando os valores do formulário
                obj = cl(**form_data)

                # Insere o novo objeto na lista de objetos da classe
                cl.insert(obj.user)
                cl.last()
                
        obj =cl.obj.get(code)
        if prev_option == 'insert' and option == 'save':
            if cl.auto_number == 1:
                strobj = "None"
            else:
                strobj = request.form[cl.att[0]]
            for i in range(1, len(cl.att)):
                strobj += ";" + request.form[cl.att[i]]
            cl.insert(getattr(obj, cl.att[0]))
            cl.last()
        elif prev_option == 'edit' and option == 'save':
            for i in range(cl.auto_number, len(cl.att)):
                att = cl.att[i]
                setattr(obj, att, request.form[att])
            cl.update(getattr(obj, cl.att[0]))
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == 'cancel':
                pass
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"))
        prev_option = option

        # Ensure obj contains the attributes to be edited
        if option == 'insert' or len(cl.lst) == 0:
            obj = {att: "" for att in cl.att}

        return render_template("gformusers1.html", butshow=butshow, butedit=butedit,
                                cname=cname, obj=obj, att=cl.att, header=cl.header, des=cl.des,
                                ulogin=session.get("user"), auto_number=cl.auto_number,
                                submenu=submenu)
    
    else:
        return render_template("index.html", ulogin=ulogin)
