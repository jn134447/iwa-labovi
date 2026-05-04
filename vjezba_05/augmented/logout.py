#!python.exe

import cgitb
import session

cgitb.enable()

print("Content-Type: text/html")
session.destroy_session()
print("Location: login.py")
print()