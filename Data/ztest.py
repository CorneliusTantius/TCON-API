# import time
# from datetime import datetime

# t =  int(time.time())
# print(t)
# print(str(datetime.fromtimestamp(t)))


import base64
from os import truncate

def encode(string):
    message_bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    del message_bytes, base64_bytes
    return base64_message

def decode(string):
    base64_bytes = string.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    del base64_bytes, message_bytes
    return message

# while True:
#     s = input("string=> ")
#     print(encode(s))
#     print("-"*20)


import sqlite3
from sqlite3 import Error

def get_connection(db_name):
	try:
		con = sqlite3.connect(db_name)
	except Error:
		con = None
		print(Error)
	return con

# with get_connection("user.db")