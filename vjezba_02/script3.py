#!C:\ProgramData\Anaconda3\python.exe

import cgi

params = cgi.FieldStorage()
student_status = {
    "status1": "Redovan",
    "status2": "Izvanredan"
    }

courses = {
    "course1": "Racunarstvo",
    "course2": "MTT",
    "course3": "Racunovodstvo",
    "course4": "Elektroteh",
    }

zavrsni = params.getvalue("zavrsni")
if zavrsni == "None":
    zavrsni = "Ne"
else:
    zavrsni = "Da"
    
note = params.getvalue("note")
if note == None:
    note = "Nema Napomena"

print("Content-type: text/html")
print()
print('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>script3</title>
  </head>
  <body>
    <h2>Uneseni podaci:</h2>
    <p>Ime: ''' + params.getvalue("name") + ''' </p>
    <p>E-mail: ''' + params.getvalue("email") + ''' </p>
    <p>Status: ''' +  student_status.get(params.getvalue("student_status")) + ''' </p>
    <p>Smjer: ''' + courses.get(params.getvalue("courses")) + ''' </p>
    <p>Zavrsni rad: ''' + zavrsni + ''' </p>
    <p>Napomene: ''' + note + ''' </p>
    <br />
    <a href="./script0.py">Na pocetak</a>
  </body>
</html>
''')