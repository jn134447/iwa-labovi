import mysql.connector
import json
import password_pomoc

# comments of wisdom:
# mydb.commit instead of returning for creating,updating,deleting from db
# return cursor fetch if just getting data
# the table here is different from the exercises as we dont need a name

db_conf = {
    "host":"localhost",
    "db_name": "obrana2registracija",
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

def get_user(email):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    if email:
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    return cursor.fetchone()

def create_user(email, password_hash):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute('INSERT INTO users (email, password) VALUES (%s, %s)', (email, password_hash))
    mydb.commit()











    