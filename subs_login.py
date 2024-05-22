# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: subs_login.py

"""""

from flask import Flask, render_template, request, session
from classes.userlogin import Userlogin


def login():
    return render_template("login.html", user= "", password="", ulogin=session.get("user"),resul = "")

def logoff():
    session.pop("user",None)
    return render_template("index.html", ulogin=session.get("user"))


def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        grupo = Userlogin.obj[user].usergroup
        session["user"] = user
        return render_template("index.html", grupo=grupo, ulogin=session.get("user"), submenu=None)
    return render_template("login.html", user=user, password=password, ulogin=session.get("user"), resul=resul, submenu=None)