#!G:/Python311/python.exe

import cgi
import cgitb
import os
import db
import password_utils
import session

cgitb.enable()

def print_form(error=None):
    print("<!doctype html>")
    print("<html lang='hr'>")
    print("<head>")
    print("<meta charset='UTF-8' />")
    print("<title>Promjena lozinke</title>")
    print("</head>")
    print("<body>")
    if error:
        print("<p style='color:red;'>" + error + "</p>")
    print("<form method='post'>")
    print("<label>Stara lozinka: <input type='password' name='old_password' /></label><br />")
    print("<label>Nova lozinka: <input type='password' name='new_password' /></label><br />")
    print("<label>Ponovi novu lozinku: <input type='password' name='new_password2' /></label><br />")
    print("<input type='submit' value='Promijeni lozinku' />")
    print("</form>")
    print("<a href='skripta.py'>Natrag</a>")
    print("</body>")
    print("</html>")

def change_password(form, session_data):
    old_password = form.getvalue("old_password", "")
    new_password = form.getvalue("new_password", "")
    new_password2 = form.getvalue("new_password2", "")

    if not old_password or not new_password or not new_password2:
        return "Sva polja su obavezna."

    if new_password != new_password2:
        return "Nove lozinke se ne podudaraju."

    user = db.get_user(email=session_data.get("user_email"))
    if user is None:
        return "Korisnik nije pronađen."

    stored_hash = bytes(user[3])
    if not password_utils.verify_password(old_password, stored_hash):
        return "Stara lozinka nije ispravna."

    new_hash = password_utils.hash_password(new_password)
    db.update_password(user[0], new_hash)

    return None

# --- main ---

form = cgi.FieldStorage()

print("Content-Type: text/html")
session_id, session_data = session.get_session_data()

if "user_id" not in session_data:
    print("Location: login.py")
    print()
else:
    if os.environ["REQUEST_METHOD"].upper() == "POST":
        error = change_password(form, session_data)
        if error is None:
            print("Location: skripta.py")
            print()
        else:
            print()
            print_form(error)
    else:
        print()
        print_form()