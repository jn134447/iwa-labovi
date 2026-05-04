import podaci
import db

def print_headers():
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

def print_navigation():
    for year_id, year_name in sorted(podaci.year_names.items()):
        print("<button type='submit' name='current_year' value='" + str(year_id) + "'>" + year_name + "</button>")

def print_one_subject(subject_id, subject_data, session_data):
    saved_value = session_data.get(subject_id, "not")

    # print("<td>" + subject_data["name"] + "</td>")
    # print("<td>" + str(subject_data["ects"]) + "</td>")
    print('''
        <tr>
            <td>''' + subject_data["name"] + '''</td>
            <td>''' + str(subject_data["ects"]) + '''</td>
            <td>
    ''')

    # first = True
    for status_id, status_name in podaci.status_names.items():
        checked = ""
        if saved_value == status_id:
            # checked = " checked='checked'"
            checked = "checked"

        # if not first:
        #     print("<br />")

        print("<label>" + status_name + "</label>")
        print("<input type='radio' name='" + subject_id + "' value='" + status_id + "' " + checked + "/>")
        # print(status_name)
        # print("</label>")

        # first = False
    print('''
            </td>
        </tr>
    ''')

def print_year_subjects(current_year, session_data, subjects):
    # print("<p>" + podaci.year_names[current_year] + "</p>")
    # print("<p>ECTS</p>")
    # print("<p>Status</p>")
    print("<tr>")
    print("<th>" + podaci.year_names[current_year] + "</th>")
    print("<th>ECTS</th>")
    print("<th>Status</th>")
    print("</tr>")

    for subject_id, subject_data in subjects.items():
        if subject_data["year"] == current_year:
            print_one_subject(subject_id, subject_data, session_data)

def print_upisni_list(session_data, subjects):
    # print("<p>Predmet</p>")
    # print("<p>ECTS</p>")
    # print("<p>Status</p>")
    print("<tr>")
    print("<th>Predmet</th>")
    print("<th>ECTS</th>")
    print("<th>Status</th>")
    print("</tr>")

    for year_id in sorted(podaci.year_names):
        if year_id == 4:
            continue

        # print("<p colspan='3'><b>" + podaci.year_names[year_id] + "</b></p>")
       

        for subject_id, subject_data in subjects.items():
            if subject_data["year"] == year_id:
                saved_value = session_data.get(subject_id, "not")

                # print("<p>" + subject_data["name"] + "</p>")
                # print("<p>" + str(subject_data["ects"]) + "</p>")
                # print("<p>" + podaci.status_names[saved_value] + "</p>")
                print("<tr>")
                print("<td>" + subject_data["name"] + "</td>")
                print("<td>" + str(subject_data["ects"]) + "</td>")
                print("<td>" + podaci.status_names[saved_value] + "</td>")
                print("</tr>")

def print_main_form(current_year, session_data, subjects):
    print("<form method='post'>")
    print("<table>")
    print_navigation()
    if current_year == 4:
        print_upisni_list(session_data, subjects)
    else:
        print_year_subjects(current_year, session_data, subjects)
    print("</table>")
    print("</form>")

def print_ukupno_ects(session_data, subjects):
    total_ects = 0
    for subject_id, subject_data in subjects.items():
        if session_data.get(subject_id) == "pass":
            total_ects += subject_data["ects"]
    print("<p>Ukupno ECTS bodova: " + str(total_ects) + "</p>")

def print_greeting(session_data):
    user = db.get_user(email=session_data.get("user_email"))
    if user:
        print("<p>Hej " + user[1] + "!</p>")