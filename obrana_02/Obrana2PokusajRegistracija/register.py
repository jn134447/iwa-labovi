#!python.exe
import base
import db
import password_pomoc
import cgi
import os

def print_form(error=None):
    base.start_html()
    if error:
        print(f'<p>error {error}</p>')
    print(f'''
    <form method="post">
        <input type="email" placeholder="email" name="email" />
        <input type="password" placeholder="password" name="password"/>
        <input type="submit" value="register"/>
    </form>
    ''')

    base.finish_html()

def register(form):
    email = form.getvalue("email", "").strip()
    password = form.getvalue("password", "")

    if not email and not password:
        return "all fields req"
    if db.get_user(email):
        return "email zauzet"
    
    password_hash = password_pomoc.hash_password(password)
    db.create_user(email, password_hash)
    return None

############

form = cgi.FieldStorage()

if os.environ["REQUEST_METHOD"] == "POST":
    print("Content-type: text/html")
    error = register(form)
    if error is None:
        print("Location: login.py")
        print()
    else:
        print()
            
        print(form)
        print_form(error)
else:
    print("Content-type: text/html")
    print()

    print(form)
    print_form()