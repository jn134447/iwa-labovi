#!C:\ProgramData\Anaconda3\python.exe

import cgi

params = cgi.FieldStorage()

print("Content-type: text/html")
print()

if params.getvalue("passwd") != params.getvalue("passwd_check"):
    print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>script1</title>
</head>
<body>
    <p>Kriva lozinka</p>
    <a href="./script0.py">Na pocetak</a>
</body>
''')



else: 
    print('''  
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>script1</title>
</head>
<body>
<form action="script2.py">
      <label>Status:</label>
      <label>Redovan:</label>
      <input type="radio" name="student_status" value="status1" />
      <label>Izvanredan:</label>
      <input type="radio" name="student_status" value="status2" />
      <br />
      <br />
      <label>E-Mail:</label>
      <input type="text" name="email" value="" /><br />
      <br />

      <label>Smjer:</label>
      <select name="courses">
        <option value="course1">Racunarstvo</option>
        <option value="course2">MTT</option>
        <option value="course3">Racunovodstvo</option>
        <option value="course4">Elektroteh</option>
      </select>
      <br /><br />
      <label>Zavrsni:</label>
      <input type="checkbox" name="zavrsni" value="zavrsni" />
      <br /><br />

      <input type="submit" value="Next" />
      
      '''
      +
      '<input type="hidden" name="name" value="' + params.getvalue("name") + '">'
      # '<input type="hidden" name="passwd" value="' + params.getvalue("passwd") + '">'
      # '<input type="hidden" name="passwd_check" value="' + params.getvalue("passwd_check") + '">'
      +
      '''
    </form>  
    </body>
</html>  
''')


