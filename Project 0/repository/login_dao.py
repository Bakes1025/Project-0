from repository.connection import get_connection
from models.login_dto import Login
import psycopg2


def select_user_byid(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM user_table WHERE user_id = {user_id};"
    
    try:
        cursor.execute(qry)
        record = None
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_login = Login(record[0],record[1],record[2])
            return user_login
            
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()

def select_user(username, password) -> Login:
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM user_table WHERE user_name  = '{username}' AND user_pass = '{password}';"
    try:
        cursor.execute(qry,(username,password))
        record = None
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_login = Login(record[0],record[1],record[2])
            print(qry)
            return user_login
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()


def new_user(username,password):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "INSERT INTO user_table VALUES (default, %s, %s) RETURNING user_id;"

    try:
        cursor.execute(qry,(username,password))
        id = cursor.fetchone()
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()
