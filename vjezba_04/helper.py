import subjects as s

def header():
    print("Content-type: text/html")
    # print()

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
    print('<input type="submit" name="list_all" value="List all" >')
        
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

def print_predmet(key, val, baked_value):
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

def table_subject_rows_for_year(all_cookies, params, year = 1):
    for key in s.subjects:
        val = s.subjects[key]
        if val["year"] != year: 
            continue

        baked_value = "not"
        # fetch param
        if params.getvalue(key) is not None:
            baked_value = params.getvalue(key)
        else:
            # fetch cookie
            baked_cookie = all_cookies.get(key)
            if baked_cookie is not None:
                baked_value = baked_cookie.value
                
        # display
        print_predmet(key, val, baked_value)

def table_subject_rows_for_year_session(session_data, params, year = 1):
    for key in s.subjects:
        val = s.subjects[key]
        if val["year"] != year: 
            continue
        
        baked_value = "not"
        # fetch param
        if params.getvalue(key) is not None:
            baked_value = params.getvalue(key)
        else:
            # from session data
            baked_data = session_data.get(key)
            if baked_data is not None:
                baked_value = baked_data
            
            

        # display
        print_predmet(key, val, baked_value)


def table_end():
    print('''
        </table>
         
        ''')

def form_start():
    print('<form method="post" action="index.py">')

def form_end():
    print('</form>')


# list_all
def la_table_start():
    print('''
        <table>
            <tr>
                <th>Predmeti</th>
                <th>Status</th>
                <th>Bodovi</th>
            </tr>
        ''')
    
def la_table_subjects_state_session(session_data, params):
    total = 0
    for key in s.subjects:

        baked_value = "not"
        # fetch param
        if params.getvalue(key) is not None:
            baked_value = params.getvalue(key)
        else:
            # from session data
            baked_data = session_data.get(key)
            if baked_data is not None:
                baked_value = baked_data

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
    return total

def la_table_subjects_state(all_cookies, params):
    total = 0
    for key in s.subjects:

        baked_value = "not"
        # fetch param
        if params.getvalue(key) is not None:
            baked_value = params.getvalue(key)
        else:
            # fetch cookie
            baked_cookie = all_cookies.get(key)
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
    return total

def la_table_end():
    print('''
        </table>
        ''')