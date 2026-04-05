#!python.exe

import cgi
import os
# from http import cookies
import helper as h
import subjects as s
import session
import db

h.header()

params = cgi.FieldStorage()

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    # modified version of add_to_session() from db
    # than in ducan_sa_kosaricom example
    # cause im not incrementing s
    session.add_to_session(params) 
    
    

session_id = session.get_or_create_session_id()
_,session_data = db.get_session(session_id)


year_id = 1
if params.getvalue("list_all") is None:
    if params.getvalue("year") is not None:
        year_id = s.year_ids[params.getvalue("year")]

print()
################ end of header ################

# print(session_data)
# print("<br />")
# print(params)
# print("<br />")

if params.getvalue("list_all") is not None:

    h.print_html_start("list all")

    h.form_start()
    h.print_year_buttons()
    h.la_table_start()
    total = h.la_table_subjects_state_session(session_data, params)
    h.la_table_end()

    print()
    print(f'<p>Total: {total}</p>')
    print()

else:
    h.print_html_start(s.year_names[year_id])

    h.form_start()
    h.print_year_buttons()
    h.table_start(year_id)
    h.table_subject_rows_for_year_session(session_data, params, year_id)
    h.table_end()


h.form_end()

h.print_html_end()

