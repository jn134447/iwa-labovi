#!python.exe

import cgi
import cgitb
import os
import db
import password_utils
import session
import helper

cgitb.enable()

def print_form(error=None):
    helper.print_html_start("Prijava")
    if error:
        print("<p style='color:red;'>" + error + "</p>")
    print('''
        <form method='post'>  
            <label>Ime: </label><input type='text' name='ime' /><br />  
            <label>Lozinka: </label><input type='password' name='password' /><br /> 
            <input type='submit' value='Prijava' /> 
        </form> 
        <a href='register.py'>Nemas racun? Registriraj se</a> 
    ''')
    helper.print_html_end();

def login(form):
    ime = form.getvalue("ime", "").strip()
    password = form.getvalue("password", "")

    if not ime or not password:
        return "Sva polja su obavezna."

    user = db.get_user(ime=ime)

    if user is None:
        return "Pogresno ime ili lozinka."

    stored_hash = bytes(user[3])
    if not password_utils.verify_password(password, stored_hash):
        return "Pogresno ime ili lozinka."

    session_id, data = session.get_session_data()
    data["user_id"] = user[0]
    data["user_email"] = user[2]
    db.update_session(session_id, data)

    return None


form = cgi.FieldStorage()

if os.environ["REQUEST_METHOD"].upper() == "POST":
    print("Content-Type: text/html")
    error = login(form)
    if error is None:
        print("Location: skripta.py")
        print()
    else:
        print()
        print_form(error)
else:
    print("Content-Type: text/html")
    print()
    print_form()