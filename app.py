from flask import Flask, render_template, request, session
from datafile import filename

import os

from classes.Residente import Residente
from classes.Reserva import Reserva
from classes.Estacionamento import Estacionamento
from classes.ResidenteAlugar import ResidenteAlugar
from classes.SalasComuns import SalasComuns
from classes.ReservaGinasio import ReservaGinasio
from classes.InscricaoGinasio import InscricaoGinasio

from classes.customer import Customer
from classes.product import Product
from classes.customerorder import CustomerOrder
from classes.orderproduct import OrderProduct
from classes.userlogin import Userlogin

app = Flask(__name__)

Residente.read(filename + 'Residencia.db')
Reserva.read(filename + 'Residencia.db')
Estacionamento.read(filename + 'Residencia.db')
ResidenteAlugar.read(filename + 'Residencia.db')
SalasComuns.read(filename + 'Residencia.db')
ReservaGinasio.read(filename + 'Residencia.db')
InscricaoGinasio.read(filename + 'Residencia.db')
Customer.read(filename + 'Residencia.db')
Product.read(filename + 'Residencia.db')
CustomerOrder.read(filename + 'Residencia.db')
OrderProduct.read(filename + 'Residencia.db')
Userlogin.read(filename + 'Residencia.db')

app.secret_key = 'BAD_SECRET_KEY'

upload_folder = os.path.join('static', 'ProductFotos')
app.config['UPLOAD'] = upload_folder

import subs_login as lsub
import subs_gform as gfsub
import subs_gform_users as gfsubusers
import subs_gform_users1 as gfsubusers1
import subs_gformT_users as gfTsubusers
import subs_gformT as gfTsub
import subs_hform as gfhsub
import subs_subform as gfsubsub
import subs_productFoto as productFotosub
import subs_mapaOrderform as mapasub
import userlogin as loginsub
import subs_mapaAlugarform as mapasub2
import subs_SalasComunsFoto as SalasComunsFotosub

@app.route("/")
def index():
    user = session.get("user")
    grupo = Userlogin.obj[user].usergroup if user else None
    return render_template("index.html", ulogin=user, grupo=grupo, submenu=None)
    


@app.route("/login")
def login():
    return lsub.login()

@app.route("/logoff")
def logoff():
    return lsub.logoff()

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        grupo = Userlogin.obj[user].usergroup
        session["user"] = user
        return render_template("index.html", grupo=grupo, ulogin=session.get("user"), submenu=None)
    return render_template("login.html", user=user, password=password, ulogin=session.get("user"), resul=resul, submenu=None)

@app.route("/submenu", methods=["post","get"])
def getsubm():
    submenu = request.args.get("subm")
    user = session.get("user")
    grupo = Userlogin.obj[user].usergroup if user else None
    return render_template("index.html", ulogin=user, grupo=grupo, submenu=submenu)

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname=''):
    submenu = request.args.get("subm")
    user = session.get("user")
    code = Userlogin.obj[user].code if user else None
    grupo = Userlogin.obj[user].usergroup if user else None
    return gfsub.gform(cname,submenu, grupo,code)

@app.route("/gformusers/<cname>", methods=["post","get"])
def gformusers(cname=''):
    submenu = request.args.get("subm")
    user = session.get("user")
    code = Userlogin.obj[user].code if user else None
    grupo = Userlogin.obj[user].usergroup if user else None
    return gfsubusers.gform(cname,submenu, grupo,code)

@app.route("/gformusers1/<cname>", methods=["post","get"])
def gformusers1(cname=''):
    submenu = request.args.get("subm")
    user = session.get("user")
    code = Userlogin.obj[user].code if user else None
    grupo = Userlogin.obj[user].usergroup if user else None
    return gfsubusers1.gform(cname,submenu, grupo,code)
    
@app.route("/gformT/<cname>", methods=["post","get"])
def gformT(cname=''):
    submenu = request.args.get("subm")
    user = session.get("user")
    code = Userlogin.obj[user].code if user else None
    grupo = Userlogin.obj[user].usergroup if user else None
    return gfTsub.gformT(cname,submenu,grupo,code)

@app.route("/gformTusers/<cname>", methods=["post","get"])
def gformTusers(cname=''):
    submenu = request.args.get("subm")
    user = session.get("user")
    code = Userlogin.obj[user].code if user else None
    grupo = Userlogin.obj[user].usergroup if user else None
    return gfTsubusers.gformT(cname,submenu,grupo,code)

@app.route("/hform/<cname>", methods=["post","get"])
def hform(cname=''):
    submenu = request.args.get("subm")
    user = session.get("user")
    grupo = Userlogin.obj[user].usergroup if user else None
    return gfhsub.hform(cname,submenu,grupo)


@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname=""):
    submenu = request.args.get("subm")
    user = session.get("user")
    grupo = Userlogin.obj[user].usergroup if user else None
    return gfsubsub.subform(cname,submenu,grupo)

@app.route("/productform", methods=["post","get"])
def productFoto():
    submenu = request.args.get("subm")
    cname = 'Product'
    return productFotosub.productFoto(app,cname,submenu)

@app.route("/ReservaGinasioform", methods=["post","get"])
def ReservaGym():
    submenu = request.args.get("subm")
    cname = 'ReservaGinasio'
    return productFotosub.productFoto(app,cname,submenu)

@app.route("/order/mapa", methods=["post","get"])
def ordermapa():
    submenu = request.args.get("subm")
    cname = ''
    return mapasub.mapaOrderform(app,cname,submenu)


@app.route("/SalasComunsform", methods=["post","get"])
def SalasComunsInsert():
    submenu = request.args.get("subm")
    cname = 'SalasComuns'
    return SalasComunsFotosub.productFoto(app,cname,submenu)

@app.route("/Alugar/mapa", methods=["post","get"])
def AlugarSalaComum():
    submenu = request.args.get("subm")
    cname = ''
    return mapasub2.mapaAlugarform(app,cname,submenu)

@app.route("/Userlogin", methods=["post","get"])
def userlogin(cname = ""):
    submenu = request.args.get("subm")
    user = session.get("user")
    grupo = Userlogin.obj[user].usergroup if user else None
    code = Userlogin.obj[user].code if user else None
    password = Userlogin.obj[user].password if user else None
    return loginsub.userlogin(cname,submenu, code,user,grupo,password)

@app.route("/Residente", methods=["post","get"])
def residente(cname = ""):
    submenu = request.args.get("subm")
    user = session.get("user")
    grupo = Userlogin.obj[user].usergroup if user else None
    code = Userlogin.obj[user].code if user else None
    password = Userlogin.obj[user].password if user else None
    return loginsub.userlogin(cname,submenu, code,user,grupo,password)

@app.route("/uc", methods=["post","get"])
def uc():
    user = session.get("user")
    grupo = Userlogin.obj[user].usergroup if user else None
    return render_template("uc.html", ulogin=user, grupo=grupo, submenu=submenu)

if __name__ == '__main__':
    app.run(debug=True, port=6001)
    #app.run()
