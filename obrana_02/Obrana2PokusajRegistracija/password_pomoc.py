import os
import hashlib
import base64

def hash_password(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    hash = salt + key 

    return hash
 