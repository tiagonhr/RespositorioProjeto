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

def userlogin():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        group = Userlogin.obj[ulogin].usergroup
        if group != "admin":
            Userlogin.current(ulogin)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        
        if option == "edit":
            butshow = "disabled"
            butedit = "enabled"
        elif option == "delete":
            obj = Userlogin.current()
            Userlogin.remove(obj.user)
            if not Userlogin.previous():
                Userlogin.first()
        elif option == "insert":
            butshow = "disabled"
            butedit = "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            obj = Userlogin(request.form["code"],request.form["user"],request.form["usergroup"], \
                            Userlogin.set_password(request.form["password"]))
            Userlogin.insert(obj.user)
            Userlogin.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Userlogin.current()
            if group == "admin":
                obj.usergroup = request.form["usergroup"]
            if request.form["password"] != "":
                obj.password = Userlogin.set_password(request.form["password"])
                print(obj.password)
            Userlogin.update(obj.user)
        elif option == "first":
            Userlogin.first()
        elif option == "previous":
            Userlogin.previous()
        elif option == "next":
            Userlogin.nextrec()
        elif option == "last":
            Userlogin.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Userlogin.current()
        if option == 'insert' or len(Userlogin.lst) == 0:
            user = ""
            usergroup = ""
            password = ""
            code = ""
        else:
            user = obj.user
            usergroup = obj.usergroup
            password = ""
        return render_template("userlogin.html", butshow=butshow, butedit=butedit, user=user,usergroup = usergroup,password=password, ulogin=session.get("user"), group=group)
    else:
      return render_template("index.html", ulogin=ulogin)