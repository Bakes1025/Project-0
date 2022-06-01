
from repository.account_dao import account_deposit, close_account, get_bank_acct, get_bank_acct_byid, new_account
from repository.login_dao import select_user


def create_new_bank(input):
    user_dto = select_user(input.get("user_name"),input.get("user_pass"))
    if user_dto is not None:
        return new_account(user_dto,input.get("acct_type"))

def deposit(input):
    account_dto = get_bank_acct(input.get("account_number"),input.get("routing_number"))
    if account_dto is not None:
        return account_deposit(account_dto.account_id,input.get("deposit_amount"))

def delete_confirm(input):
    account_dto = get_bank_acct(input.get("account_number"),input.get("routing_number"))
    if account_dto is not None:
        return close_account(account_dto.account_id)
    