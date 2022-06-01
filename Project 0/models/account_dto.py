import re


class Account:
    def __init__(self,account_id,user_id,account_number, routing_number, account_type,balance):
       self.account_id = account_id
       self.user_id = user_id
       self.account_number = account_number
       self.routing_number = routing_number
       self.account_type = account_type
       self.balance = balance

    def __repr__(self) -> str:
        return f"Account Number: {self.account_number}, Routing Number: {self.routing_number}, Type: {self.account_type} -- Balance: {self.balance}"

    def overdraw(self) -> bool:
        if self.balance < 0:
            return True