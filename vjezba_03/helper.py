import subjects as s

def header():
    print("Content-type: text/html")
    print()

def print_html_start(title=""):
    print('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>''' + title + '''</title>
    </head>
    <body>
    ''')

def print_html_end():
    print('''
    </body>
    </html>
    ''')

def print_year_buttons():
    for key in s.year_names:
        val = s.year_names[key]
        print('<input type="submit" name="year" value="'+ val +'" >')
        
def table_start(year = 1):
    val = s.year_names[year]
    print('''
        <table>
            <tr>
                <th>''' + val + '''</th>
                <th>ECTS</th>
                <th>Status</th>
            </tr>
        ''')

def table_subject_rows_for_year(all_cookies, year = 1):
    for key in s.subjects:
        baked_cookie = all_cookies.get(key)
        baked_value = "not"
        if baked_cookie is not None:
            baked_value = baked_cookie.value
        val = s.subjects[key]
        if val["year"] != year: 
            continue
        print('''
            <tr>
                <td>''' + val["name"] + '''</td>
                <td>''' + str(val["ects"]) + '''</td>
                <td>''')
        for status in s.status_names:
            print(f'<label>{s.status_names.get(status)}</label>')
            print(f'<input type="radio" name="{key}" value="{status}" {"checked" if baked_value == status else ""}/>')
        print('''
                </td>
            </tr>
        ''')

def table_end():
    print('''
        </table>
        <a href="./list_all.py">List all</a>
        ''')

def form_start():
    print('<form method="post" action="index.py">')

def form_end():
    print('</form>')