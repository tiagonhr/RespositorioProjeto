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
from classes.residente import residente

from classes.gclass import Gclass
prev_option = ""

def residente(cname='', submenu="", code = "",user = "", grupo="",password =""):
    global prev_option
    ulogin=session.get("user")

    if (grupo == "admin"):

        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        
        if option == "edit":
            butshow = "disabled"
            butedit = "enabled"
        elif option == "delete":
            obj = residente.current()
            residente.remove(obj.user)
            if not residente.previous():
                residente.first()
        elif option == "insert":
            butshow = "disabled"
            butedit = "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            obj = residente.get(code)
            residente.insert(obj.user)
            residente.last()
        elif prev_option == 'edit' and option == 'save':
            obj = residente.current()
            
            residente.update(obj.user)
        elif option == "first":
            residente.first()
        elif option == "previous":
            residente.previous()
        elif option == "next":
            residente.nextrec()
        elif option == "last":
            residente.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = residente.current()
        if option == 'insert' or len(residente.lst) == 0:
            user = ""
            usergroup = ""
            password = ""
            code = ""
        else:
            user = obj.user
            usergroup = obj.usergroup
            password = ""
        return render_template("residente.html", butshow=butshow, butedit=butedit, user=user,usergroup = usergroup,password=password, ulogin=session.get("user"), group=group)
    
    elif grupo == "users":
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")

        # Filtra pelo usuário fornecido

        obj = residente.obj.get(user)

        if not obj:
            return render_template("error.html", message="User not found.")

        if option == "edit":
            butshow = "disabled"
            butedit = "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'edit' and option == 'save':
            if request.form["password"]:
                obj.password = residente.set_password(request.form["password"])
            residente.update(obj.user)
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))

        prev_option = option

        if option == 'insert' or len(residente.lst) == 0:
            user = ""
            usergroup = ""
            password = ""
            code = ""
        else:
            user = obj.user
            usergroup = obj.usergroup
            code = obj.code
            password = ""

        return render_template("residente.html", butshow=butshow, butedit=butedit, code=code, user=user, usergroup=usergroup, password=password, ulogin=session.get("user"), group=grupo)

    else:
        return render_template("index.html", ulogin=ulogin)