#!python.exe

import cgi
import cgitb
import db
import password_utils
import session
import helper
import os

cgitb.enable()

def print_headers():
    print("Content-Type: text/html")
    print()

def print_form(error=None):
    helper.print_html_start("Registracija")
    if error:
        print("<p style='color:red;'>" + error + "</p>")
    print('''
        <form method='post'>
            <label>Ime: </label><input type='text' name='ime' /><br />
            <label>E-mail: </label><input type='email' name='email' /><br />
            <label>Lozinka: </label><input type='password' name='password' /><br />
            <label>Ponovi lozinku: </label><input type='password' name='password2' /><br />
            <input type='submit' value='Registracija' />
        </form>
        <a href='login.py'>Vec imas racun? Prijavi se</a>
    ''')
    helper.print_html_end()

def register(form):
    ime = form.getvalue("ime", "").strip()
    email = form.getvalue("email", "").strip()
    password = form.getvalue("password", "")
    password2 = form.getvalue("password2", "")

    if not ime or not email or not password:
        return "Sva polja su obavezna."

    if password != password2:
        return "Lozinke se ne podudaraju."

    if db.get_user(ime=ime):
        return "Ime je vec zauzeto."

    if db.get_user(email=email):
        return "E-mail je vec zauzet."

    password_hash = password_utils.hash_password(password)
    db.create_user(ime, email, password_hash)
    return None


form = cgi.FieldStorage()

if os.environ["REQUEST_METHOD"].upper() == "POST":
    print("Content-Type: text/html")
    error = register(form)
    if error is None:
        print("Location: login.py")
        print()
    else:
        print()
        print_form(error)
else:
    print("Content-Type: text/html")
    print()
    print_form()