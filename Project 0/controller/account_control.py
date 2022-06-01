
from flask import render_template
from repository.account_dao import get_bank_acct, get_bank_acct_byid
from repository.login_dao import select_user, select_user_byid
from service.account_service import create_new_bank, delete_confirm, deposit

def generate_account_form():
    return render_template("account_type.html")

def create_new_account(input):
    account_dto = create_new_bank(input)
    user_dto = select_user(input.get("user_name"),input.get("user_pass"))
    print(user_dto)
    if  account_dto is not None:
        new_acct = get_bank_acct_byid(account_dto)
        return render_template("account_success.html",accnum = new_acct.account_number,routing = new_acct.routing_number,id = user_dto.user_id)
    else:
        return "An error has occurred"

def request_deposit(input):
    try:
        deposit_confirm = deposit(input)
        if int(input.get("deposit_amount")) < 0 or deposit_confirm is None:
            return render_template("failed_deposit.html")
        account_dto = get_bank_acct(input.get("account_number"),input.get("routing_number"))
        if deposit_confirm is not None:
            return render_template("deposit_success.html",amount = input.get("deposit_amount"),new_balance = account_dto.balance, accnum = account_dto.account_number,routing = account_dto.routing_number,id = account_dto.user_id)
    except(TypeError,ValueError):
        return render_template("failed_deposit.html")

def request_delete(input):
    account_dto = get_bank_acct(input.get("account_number"),input.get("routing_number"))

    if account_dto is not None:
        delete_confirm(input)
        return render_template("account_closed.html",username = select_user_byid(account_dto.user_id).username)