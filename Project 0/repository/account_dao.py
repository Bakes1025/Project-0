import random
from flask import render_template
import psycopg2
from models.account_dto import Account
from models.login_dto import Login
from repository.connection import get_connection


def new_account(login_dto:Login,account_type):
    connection = get_connection()
    cursor = connection.cursor()
    account_number = "%0.10d" % random.randint(0,9999999999)
    routing_number = "%0.9d" % random.randint(0,999999999)
    qry = "INSERT INTO account_table VALUES (default,%s,%s,%s,%s,0) RETURNING account_id;"

    try:
        cursor.execute(qry,(login_dto.user_id,account_number,routing_number,account_type))
        account_id = cursor.fetchone()[0]
        connection.commit()
        return account_id
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()

def get_bank_acct(account_number:int,routing_number:int):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM account_table WHERE account_number = '{account_number}' and routing_number = '{routing_number}';"
    
    try:
        cursor.execute(qry)
        record = None
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            account_info = Account(record[0],record[1],record[2],record[3],record[4],record[5])
            connection.commit()
            return account_info

    except(psycopg2.DatabaseError,TypeError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()

def get_bank_acct_byid(account_id:int) -> Account:
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM account_table WHERE account_id = {account_id};"
    
    try:
        cursor.execute(qry)
        record = None
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            account_info = Account(record[0], record[1],record[2],record[3],record[4],record[5])
            connection.commit()
            return account_info

    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()

def account_deposit(account_id,amount):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        if int(amount) >= 0:
            qry = f"UPDATE account_table SET balance=balance+{amount} WHERE account_id={account_id} returning balance;"

            
            cursor.execute(qry)
            record = None
            while True:
                    record = cursor.fetchone()
                    if record is None:
                        break
                    new_balance = record
                    connection.commit()
                    return new_balance

    except(psycopg2.DatabaseError,ValueError):
        return render_template("failed_deposit.html")
        
    finally:
        if connection is not None:
            connection.close()
        else:
            return None

def close_account(account_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"DELETE FROM account_table WHERE account_id = {account_id};"
    
    try:
        cursor.execute(qry)
        print(qry)
        connection.commit()
        return "Account Closed"

    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()