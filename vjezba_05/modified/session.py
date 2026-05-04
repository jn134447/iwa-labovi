import db
import os
from http import cookies

def get_or_create_session_id():
    raw_cookie = os.environ.get("HTTP_COOKIE", "")
    cookie = cookies.SimpleCookie(raw_cookie)

    session_id = None
    if cookie.get("session_id"):
        session_id = cookie["session_id"].value

    if session_id is None:
        session_id = db.create_session()
        out_cookie = cookies.SimpleCookie()
        out_cookie["session_id"] = str(session_id)
        print(out_cookie.output())

    return session_id

def get_session_data():
    session_id = get_or_create_session_id()
    _, data = db.get_session(session_id)
    return session_id, data

def save_post_to_session(form):
    session_id = get_or_create_session_id()
    _, data = db.get_session(session_id)

    import podaci
    for subject_id in db.get_subjects():
        value = form.getvalue(subject_id)
        if value is not None:
            data[subject_id] = value

    current_year = form.getvalue("current_year")
    if current_year is not None:
        data["current_year"] = current_year

    if "current_year" not in data:
        data["current_year"] = "1"

    db.update_session(session_id, data)

def destroy_session():
    raw_cookie = os.environ.get("HTTP_COOKIE", "")
    cookie = cookies.SimpleCookie(raw_cookie)
    if cookie.get("session_id"):
        session_id = cookie["session_id"].value
        db.delete_session(session_id)

    out_cookie = cookies.SimpleCookie()
    out_cookie["session_id"] = ""
    out_cookie["session_id"]["expires"] = "Thu, 01 Jan 1970 00:00:00 GMT"
    print(out_cookie.output())

def require_login():
    session_id, data = get_session_data()
    if "user_id" not in data:
        print("Content-Type: text/html")
        print("Location: login.py")
        print()
        exit()