#!G:\Python311\python.exe

import mysql.connector


db_conf = {
    "host":"localhost",
    "db_name": "zadatakSesija",
    "user":"root",
    "passwd":""
}

def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["db_name"]
    )
    return mydb


def create_session():
    mydb = get_DB_connection()
    cursor = mydb.cursor()

    query = "INSERT INTO sessions (data) VALUES (%s)"
    value = ('hr',)

    cursor.execute(query, value)
    mydb.commit()

    return cursor.lastrowid


def get_session_data(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()

    query = "SELECT * FROM sessions WHERE session_id = %s"
    values = (session_id,)
    cursor.execute(query, values)

    result = cursor.fetchone()

    return result[0], result[1]


def update_session(session_id, data):
    mydb = get_DB_connection()
    cursor = mydb.cursor()

    query = "UPDATE sessions SET data = %s WHERE session_id = %s"
    values = (data, session_id)

    cursor.execute(query, values)
    mydb.commit()





    