import psycopg2

def get_connection():
    connection = psycopg2.connect(
        database = "postgres",
        user = "postgres",
        password = "Steam1998",
        host = "project-0.csqmpqer3gcj.us-east-2.rds.amazonaws.com",
        port = "5432"
    )
    return connection
    