#!G:/Python311/python.exe

import cgi
import cgitb
import db
import password_utils
import session

cgitb.enable()

def print_headers():
    print("Content-Type: text/html")
    print()

def print_form(error=None):
    print("<!doctype html>")
    print("<html lang='hr'>")
    print("<head>")
    print("<meta charset='UTF-8' />")
    print("<title>Registracija</title>")
    print("</head>")
    print("<body>")
    if error:
        print("<p style='color:red;'>" + error + "</p>")
    print("<form method='post'>")
    print("<label>Ime: <input type='text' name='ime' /></label><br />")
    print("<label>E-mail: <input type='email' name='email' /></label><br />")
    print("<label>Lozinka: <input type='password' name='password' /></label><br />")
    print("<label>Ponovi lozinku: <input type='password' name='password2' /></label><br />")
    print("<input type='submit' value='Registracija' />")
    print("</form>")
    print("<a href='login.py'>Već imaš račun? Prijavi se</a>")
    print("</body>")
    print("</html>")

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
        return "Ime je već zauzeto."

    if db.get_user(email=email):
        return "E-mail je već zauzet."

    password_hash = password_utils.hash_password(password)
    db.create_user(ime, email, password_hash)
    return None


form = cgi.FieldStorage()

import os
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