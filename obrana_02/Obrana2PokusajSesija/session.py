#!G:\Python311\python.exe
import os
import db
from podaci import translations
from http import cookies


def get_or_create_session_id():
    raw_cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE", ""))
    session_id = None

    if "session_id" in raw_cookie:
        session_id = raw_cookie["session_id"].value
    else:
        session_id = db.create_session()
        out_cookie = cookies.SimpleCookie()
        out_cookie["session_id"] = str(session_id)
        print(out_cookie.output())
    return session_id


def get_session():
    session_id = get_or_create_session_id()
    session_id, data = db.get_session_data(session_id)
    return session_id, data


def save_post_to_session(form):
    session_id = get_or_create_session_id()
    language = form.getvalue('lang')
    if language is not None:
        db.update_session(session_id, language)

