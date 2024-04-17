from flask import Flask, render_template, request, session
from datafile import filename

import os

from classes.customer import Customer
from classes.product import Product
from classes.customerorder import CustomerOrder
from classes.orderproduct import OrderProduct
from classes.userlogin import Userlogin

app = Flask(__name__)

Customer.read(filename + 'business.db')
Product.read(filename + 'business.db')
CustomerOrder.read(filename + 'business.db')
OrderProduct.read(filename + 'business.db')
Userlogin.read(filename + 'business.db')
prev_option = ""
app.secret_key = 'BAD_SECRET_KEY'

upload_folder = os.path.join('static', 'ProductFotos')
app.config['UPLOAD'] = upload_folder


import subs_login as lsub
import subs_gform as gfsub
import subs_gformT as gfTsub
import subs_hform as gfhsub
import subs_subform as gfsubsub
import subs_productFoto as productFotosub


@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
    
@app.route("/login")
def login():
    return lsub.login()

@app.route("/logoff")
def logoff():
    return lsub.logoff()

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    return lsub.chklogin()

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname=''):
     return gfsub.gform(cname)

@app.route("/gformT/<cname>", methods=["post","get"])
def gformT(cname=''):
    return gfTsub.gformT(cname)

@app.route("/hform/<cname>", methods=["post","get"])
def hform(cname=''):
    return gfhsub.hform(cname)


        
@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname=""):
    return gfsubsub.subform(cname)


@app.route("/productform", methods=["post","get"])
def productFoto():
    cname = 'Product'
    return productFotosub.productFoto(app,cname)

    
if __name__ == '__main__':
    app.run(debug=True)
    #app.run()