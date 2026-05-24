#!G:\Python311\python.exe
from podaci import translations
import session
import cgitb
cgitb.enable()

session_id, language = session.get_session()

def start_html():
    print("<!doctype html>")
    print("<html lang='en'>")
    print("<head>")
    print("<meta charset='UTF-8' />")
    print("<meta name='viewport' content='width=device-width, initial-scale=1.0' />")
    print("<title>Document</title>")
    print("</head>")
    print("<body>")

def end_html():
    print("</body>")
    print("</html>")

print("Content-type: text/html")
print()
start_html()
for key, value in translations.items():
    if key == language:
        print(f"<a href=''>{value['index']}</a>")
        print(f"<a href=''>{value['articles']}</a>")
        print(f"<a href=''>{value['basket']}</a>")
        print(f"<a href=''>{value['contact']}</a>")

end_html()
