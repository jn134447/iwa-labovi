#!C:\ProgramData\Anaconda3\python.exe

import cgi
import os
from http import cookies
import helper as h
import subjects as s

h.header()

params = cgi.FieldStorage()

cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies = cookies.SimpleCookie(cookies_string)

if os.environ["REQUEST_METHOD"].upper() == "POST":
    cookie = cookies.SimpleCookie()
    for key in params.keys():
        if key != "year":
            cookie[key] = params.getvalue(key)
 
    print(cookie.output())

print() # header end

year_id = 1
if params.getvalue("list_all") is None:
    if params.getvalue("year") is not None:
        year_id = s.year_ids[params.getvalue("year")]

#print(params)
#print(all_cookies)

if params.getvalue("list_all") is not None:

    h.print_html_start("list all")

    h.form_start()
    h.print_year_buttons()
    h.la_table_start()
    total = h.la_table_subjects_state(all_cookies, params)
    h.la_table_end()

    print()
    print(f'<p>Total: {total}</p>')
    print()

else:
    h.print_html_start(s.year_names[year_id])

    h.form_start()
    h.print_year_buttons()
    h.table_start(year_id)
    h.table_subject_rows_for_year(all_cookies, params, year_id)
    h.table_end()


h.form_end()

h.print_html_end()

