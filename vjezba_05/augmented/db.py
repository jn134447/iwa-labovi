import mysql.connector # "C:\ProgramData\Anaconda3\python.exe" -m pip install mysql-connector 
import json

db_conf = {
    "host":"localhost",
    "db_name": "jnkiwavj5",
    "user":"root",
    "passwd":""
}

def get_DB_connection():
    return mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        password=db_conf["passwd"],
        database=db_conf["db_name"]
    )

def create_session():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = "INSERT INTO sessions (data) VALUES (%s)"
    values = (json.dumps({}),)
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid

def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = "SELECT session_id, data FROM sessions WHERE session_id = %s"
    cursor.execute(query, (session_id,))
    result = cursor.fetchone()
    return result[0], json.loads(result[1]) # type: ignore

def update_session(session_id, data):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = "UPDATE sessions SET data = %s WHERE session_id = %s"
    cursor.execute(query, (json.dumps(data), session_id))
    mydb.commit()

def delete_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM sessions WHERE session_id = %s", (session_id,))
    mydb.commit()

def create_user(ime, email, password_hash):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "INSERT INTO users (ime, email, password) VALUES (%s, %s, %s)",
        (ime, email, password_hash)
    )
    mydb.commit()
    return cursor.lastrowid

def get_user(ime=None, email=None):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    if email:
        cursor.execute("SELECT id, ime, email, password FROM users WHERE email = %s", (email,))
    else:
        cursor.execute("SELECT id, ime, email, password FROM users WHERE ime = %s", (ime,))
    return cursor.fetchone()

def get_subjects():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT id, kod, ime, bodovi, godina FROM subjects")
    rows = cursor.fetchall()
    subjects = {}
    for row in rows: # type: ignore
        subjects[row[1]] = {
            "name": row[2],
            "ects": row[3],
            "year": row[4]
        }
    return subjects


def update_password(user_id, new_hash):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "UPDATE users SET password = %s WHERE id = %s",
        (new_hash, user_id)
    )
    mydb.commit()