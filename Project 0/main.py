from flask import Flask, request
from controller.account_control import *
from repository.login_dao import *
from controller.home_control import *
from controller.login_control import *
from controller.registration_control import *

dataApp = Flask(__name__)

#RENDER TEMPLATES FOR MAINMENU, LOGIN, HOME, CREATEUSER, CREATEACCOUNT, DELETEACCOUNT, VIEWACCOUNTS
@dataApp.route('/', methods = ["GET","POST"])
def landing():
    return get_home_page()

@dataApp.route('/login',methods=["GET"])
def login():        
    return get_login_page()

@dataApp.route('/login/user', methods = ["POST","GET"])
def login_validate():
    if request.method == "POST":
        login_info = login_check_by_id(request.form)
        if login_info is not None:
            return redirect(url_for('.account_page',userid = login_info))
        else:
            return valid_login_check_byid(login_info)
    elif request.method == "GET":
        return get_login_page()

@dataApp.route('/login/<int:userid>', methods = ["GET"])
def account_page(userid):
    if valid_login_check_byid(userid) is not None:
        return load_acct_page(select_user_byid(userid).username)

@dataApp.route('/registration',methods=["GET"])
def createuser():
    return get_register_page()

@dataApp.route('/registration/register',methods = ["POST"])
def new_user():
    return register_user(request.form)

@dataApp.route('/user/delete',methods = ["GET"])
def deleteAccount():
    return render_template("accountDeletetion.html")

@dataApp.route('/user/delete/confirm',methods = ["GET","POST"])
def confirmDelete():
    return delete_account_confirm(request.form)

@dataApp.route('/createBank',methods = ["GET"])
def createBank():
    return generate_account_form()

@dataApp.route('/account/success', methods = ["POST"])
def creationSuccess(): 
    return create_new_account(request.form)

@dataApp.route('/account/deposit', methods = ["GET"])
def deposit(): 
    return render_template("deposit_form.html")

@dataApp.route('/deposit/success', methods = ["GET","POST"])
def depositSuccess(): 
    return request_deposit(request.form)

@dataApp.route('/account/close',methods = ["GET"])
def delete_accountInfo():
    return render_template("delete_request.html")

@dataApp.route('/account/close/success', methods = ["POST"])
def delete_account():
    return request_delete(request.form)

if __name__ == "__main__":
    dataApp.run(debug=True)
