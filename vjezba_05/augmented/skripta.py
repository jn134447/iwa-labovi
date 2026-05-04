#!python.exe

import helper
import session
import cgi
import db

print("Content-Type: text/html")

form = cgi.FieldStorage()
session.save_post_to_session(form)
session_id, session_data = session.get_session_data()

if "user_id" not in session_data:
    print("Location: login.py")
    print()
    exit()

print()

subjects = db.get_subjects()
current_year = int(session_data.get("current_year", "1"))

helper.print_html_start("Odabir predmeta")
helper.print_greeting(session_data)
print("<a href='logout.py'>Odjava</a>")
print("<a href='change_password.py'>Promjena Lozinke</a>")
helper.print_main_form(current_year, session_data, subjects)
helper.print_ukupno_ects(session_data, subjects)
helper.print_html_end()