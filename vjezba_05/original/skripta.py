#!G:/Python311/python.exe
import podaci
import session
import db
import cgi
import cgitb

cgitb.enable()

def print_headers():
    print("Content-Type: text/html")
    print()

def print_page_start():
    print("<!doctype html>")
    print("<html lang='hr'>")
    print("<head>")
    print("<meta charset='UTF-8' />")
    print("<meta name='viewport' content='width=device-width, initial-scale=1.0' />")
    print("<title>Odabir predmeta</title>")
    print("<style>")
    print("table, td, th { border: 1px solid black; padding: 6px; border-collapse: collapse; }")
    print("</style>")
    print("</head>")
    print("<body>")

def print_page_end():
    print("</body>")
    print("</html>")

def print_navigation():
    print("<tr>")
    for year_id, year_name in sorted(podaci.year_names.items()):
        print("<td>")
        print("<button type='submit' name='current_year' value='" + str(year_id) + "'>" + year_name + "</button>")
        print("</td>")
    print("</tr>")

def print_one_subject(subject_id, subject_data, session_data):
    saved_value = session_data.get(subject_id, "not")

    print("<tr>")
    print("<td>" + subject_data["name"] + "</td>")
    print("<td>" + str(subject_data["ects"]) + "</td>")
    print("<td>")

    first = True
    for status_id, status_name in podaci.status_names.items():
        checked = ""
        if saved_value == status_id:
            checked = " checked='checked'"

        if not first:
            print("<br />")

        print("<label>")
        print("<input type='radio' name='" + subject_id + "' value='" + status_id + "'" + checked + " />")
        print(status_name)
        print("</label>")

        first = False

    print("</td>")
    print("</tr>")

def print_year_subjects(current_year, session_data, subjects):
    print("<tr>")
    print("<th>" + podaci.year_names[current_year] + "</th>")
    print("<th>ECTS</th>")
    print("<th>Status</th>")
    print("</tr>")

    for subject_id, subject_data in subjects.items():
        if subject_data["year"] == current_year:
            print_one_subject(subject_id, subject_data, session_data)

def print_upisni_list(session_data, subjects):
    print("<tr>")
    print("<th>Predmet</th>")
    print("<th>ECTS</th>")
    print("<th>Status</th>")
    print("</tr>")

    for year_id in sorted(podaci.year_names):
        if year_id == 4:
            continue

        print("<tr>")
        print("<td colspan='3'><b>" + podaci.year_names[year_id] + "</b></td>")
        print("</tr>")

        for subject_id, subject_data in subjects.items():
            if subject_data["year"] == year_id:
                saved_value = session_data.get(subject_id, "not")
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

print_page_start()
print_greeting(session_data)
print("<a href='logout.py'>Odjava</a>")
print_main_form(current_year, session_data, subjects)
print_ukupno_ects(session_data, subjects)
print_page_end()