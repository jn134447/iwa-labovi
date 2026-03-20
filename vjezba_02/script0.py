#!C:\ProgramData\Anaconda3\python.exe


print("Content-type: text/html")
print()
print('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>script0</title>
  </head>
  <body>
    <form action="script1.py">
      <label>Ime:</label>
      <input type="text" name="name" value="" /><br /><br />
      <label>Lozinka:</label>
      <input type="text" name="passwd" value="" /><br /><br />
      <label>Ponovi lozinku:</label>
      <input type="text" name="passwd_check" value="" /><br /><br />
      <input type="submit" value="Next" />
    </form>
  </body>
</html>
''')

