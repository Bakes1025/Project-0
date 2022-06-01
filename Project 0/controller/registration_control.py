from flask import render_template
from service.login_service import *
from service.register_service import *

def get_register_page():
    return render_template("newUser.html")

def register_user(registry):
    if validate_register(registry):
        create_user(registry)
        return render_template("login.html")
    else:
        return render_template("failedRegistration.html")

def delete_account_confirm(info):
    return delete_login(info)
    
