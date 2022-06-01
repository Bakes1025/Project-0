from flask import redirect, render_template, url_for
from models.login_dto import Login
from repository.login_dao import select_user, select_user_byid
from service.login_service import login_check

def get_login_page():
    return render_template("login.html")

def load_acct_page(user):
    login_dto = Login(0,user,0)
    return render_template("userAccountHome.html", username = login_dto.username)

def valid_login_check(login_input):
    if login_check(login_input) is not None:
        return load_acct_page(login_input)
    return render_template("failedLogin.html")

def valid_login_check_byid(login_input):
    if select_user_byid(login_input) is not None:
        return load_acct_page(login_input)
    return render_template("failedLogin.html")


