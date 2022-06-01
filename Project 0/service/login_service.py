from select import select
from flask import redirect, render_template, url_for
from models.login_dto import Login
from repository.login_dao import select_user, select_user_byid

def login_check(login_input):
    user_dto = select_user(login_input.get("user_name"),login_input.get("user_pass"))
    if user_dto is not None and user_dto.validate_login():
        return user_dto
    else:
        return render_template("failedLogin.html")

def login_check_by_id(login_input):
    user_dto = select_user(login_input.get("user_name"),login_input.get("user_pass"))
    if user_dto is not None:
        return user_dto.user_id
    else:
        return None



