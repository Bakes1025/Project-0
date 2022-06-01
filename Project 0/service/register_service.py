
from flask import render_template
from models import login_dto
from models.login_dto import Login
from models.user_info_dto import User
from repository.login_dao import new_user, select_user
from repository.user_info_dao import delete_user, new_user_info

def validate_register(input):
    login_dto = Login(0,input.get("user_name"), input.get("user_pass"))
    info_dto = User(0,0, input.get("first_name"), input.get("last_name"))

    if(login_dto.validate_login() and info_dto.validate_user_info()):
        return login_dto

def validate_user_info(input):
    login_dto = Login(0,input.get("user_name"), input.get("user_pass"))
    info_dto = User(0,0, input.get("first_name"), input.get("last_name"))

    if(login_dto.validate_login() and info_dto.validate_user_info()):
        return info_dto

def create_user(input):
    if select_user(input.get("user_name"),input.get("user_pass")) == None :
        return render_template("failedRegistration.html")
    else:
        user_dto = new_user(input.get("user_name"),input.get("user_pass"))
        if user_dto is not None:
            login_dto = Login(user_dto,input.get("user_name"), input.get("user_pass"))
            user_info = new_user_info(login_dto,input.get("first_name"),input.get("last_name"))
            if user_info is not None and user_info is not None:
                return user_info
    
def delete_login(input):
    user_dto = select_user(input.get("user_name"),input.get("user_pass"))
    if user_dto is None:
        return render_template("failedDeletion.html")
    else:
        delete_user(user_dto.user_id)
        return render_template("landing.html")

###INSERT REGEX FOR REGISTRATION CHECKING (REVIEW 5/27 VIDEO)!!!!!!###########