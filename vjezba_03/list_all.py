#!C:\Users\whiisper\AppData\Local\Programs\Python\Python311\python.exe

import os
from http import cookies
import helper as h
import subjects as s

cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies = cookies.SimpleCookie(cookies_string)

def la_table_start():
    print('''
        <table>
            <tr>
                <th>Predmeti</th>
                <th>Status</th>
                <th>Bodovi</th>
            </tr>
        ''')
    
def la_table_subjects_state():
    total = 0
    for key in s.subjects:

        baked_cookie = all_cookies.get(key)
        baked_value = "not"
        if baked_cookie is not None:
            baked_value = baked_cookie.value

        val = s.subjects[key]
        print('''
            <tr>
                <td>''' + val["name"] + '''</td>
                <td>''' + s.status_names[baked_value] + '''</td>
                <td>''' + str(val["ects"]) + '''</td>
            </tr>
        ''')
        if baked_value == "pass":
            total += val["ects"]
    return total;

def la_table_end():
    print('''
        </table>
        ''')
    
h.header()
h.print_html_start("list_all")

la_table_start()
total = la_table_subjects_state()
la_table_end()

print()
print(f'<p>Total: {total}</p>')
print()

h.print_html_end()