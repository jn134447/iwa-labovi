#!C:\Users\whiisper\AppData\Local\Programs\Python\Python311\python.exe

import cgi
import os
from http import cookies
import helper as h
import subjects as s

params = cgi.FieldStorage()

cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies = cookies.SimpleCookie(cookies_string)

if os.environ["REQUEST_METHOD"].upper() == "POST":
    cookie = cookies.SimpleCookie()
    for key in params.keys():
        if key != "year":
            cookie[key] = params.getvalue(key)
    print(cookie.output())

year_id = 1
if params.getvalue("year") != None:
    year_id = s.year_ids[params.getvalue("year")]

h.header()
h.print_html_start(s.year_names[year_id])

h.form_start()
h.print_year_buttons()

h.table_start(year_id)
h.table_subject_rows_for_year(all_cookies, year_id)


h.table_end()
h.form_end()

h.print_html_end()

