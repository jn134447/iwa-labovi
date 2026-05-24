#!G:\Python311\python.exe
import os
from podaci import translations
import session
import cgi
import cgitb
cgitb.enable()


form = cgi.FieldStorage()
session.save_post_to_session(form)

session_id, language_value = session.get_session()

def start_html():
    print("<!doctype html>")
    print("<html lang='en'>")
    print("<head>")
    print("<meta charset='UTF-8' />")
    print("<meta name='viewport' content='width=device-width, initial-scale=1.0' />")
    print("<title>Document</title>")
    print("</head>")
    print("<body>")
    print("<form method='post'>")

def end_html():
    print("<br><button type='submit'>Spremi promjene</button>")
    print("</form>")
    print("<br><a href='prijevod.py'>Prikazi prijevod</a>")
    print("</body>")
    print("</html>")

def print_navigation(lang_value):
    print("<div>")
    for key, value in translations.items():
        if lang_value == key:
            print(f"<a href=''>{value['index']}</a>")
            print(f"<a href=''>{value['articles']}</a>")
            print(f"<a href=''>{value['basket']}</a>")
            print(f"<a href=''>{value['contact']}</a>")
    print("</div><br>")
    

def print_choices(lang_value):
    for key in translations:
        checked = ""
        if key == lang_value:
            checked = "checked"
        print(f"<input type='radio' name='lang' value='{key}' {checked}>{key}")
    print("<br>")


print("Content-type: text/html")
print()
start_html()
print_navigation(language_value)
print_choices(language_value)
end_html()