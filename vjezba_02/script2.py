#!C:\ProgramData\Anaconda3\python.exe

import cgi

params = cgi.FieldStorage()
# name = params.getvalue("name")
# passwd = params.getvalue("passwd")
# passwd_check = params.getvalue("passwd_check")



print("Content-type: text/html")
print()
print('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>script2</title>
  </head>
  <body> 
  <form action="script3.py">
      <label>Napomena:</label>
      <textarea name="note" value="" rows="4" cols="50"></textarea>
      <br />
      <br />
      <input type="submit" value="Next" />
      '''
      +
       '<input type="hidden" name="name" value="' + params.getvalue("name") + '">'
       # '<input type="hidden" name="passwd" value="' + params.getvalue("passwd") + '">'
       # '<input type="hidden" name="passwd_check" value="' + params.getvalue("passwd_check") + '">'
       '<input type="hidden" name="student_status" value="' + params.getvalue("student_status") + '">'
       '<input type="hidden" name="email" value="' + params.getvalue("email") + '">'
       '<input type="hidden" name="courses" value="' + params.getvalue("courses") + '">'
       '<input type="hidden" name="zavrsni" value="' + str(params.getvalue("zavrsni")) + '">' # causes concat issues with NoneType and str
       +
      '''
    </form>
  </body>
</html>   
''')  
