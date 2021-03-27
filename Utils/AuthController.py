import uuid
import base64
import sqlite3
from sqlite3 import Error

def get_connection(db_name):
	try:
		con = sqlite3.connect(db_name)
	except Error:
		con = None
		print(Error)
	return con

def base64_encoding(string):
    message_bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    del message_bytes, base64_bytes
    return base64_message

def base64_decoding(string):
    base64_bytes = string.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    del base64_bytes, message_bytes
    return message

def register_user(data):
    # data required: firstName, lastName, email, phoneNumber, password
    print("Registering new user")
    con = get_connection('Utils/DB/user.db')
    if con != None:
        cur = con.cursor()
        try:
            em = data['email']
        except:
            return "Email Cannot Be Empty"
        query = f"SELECT ID FROM user WHERE Email = \'{em}\';"
        cur.execute(query)
        if len(cur.fetchall()) != 0:
            return "Email Already Exists"
        
        try:
            pn = data['phoneNumber']
        except:
            return "Phone Number Cannot Be Empty"
        query = f'SELECT PhoneNumber FROM user WHERE PhoneNumber = \'{pn}\';'
        if len(cur.fetchall()) != 0:
            return "Phone Number Already Exists "

        new_id = str(uuid.uuid1())
        try:
            entities = (new_id, data['firstName'],
                data['lastName'], data['email'],
                data['phoneNumber'], 
                base64_encoding(data['password']),
                0, "")
        except:
            return "Parameter / Payload Error"
        query = "INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, entities)
        con.commit()
        del data, con, cur, new_id, entities, query
        return "Done"
    else:
        return "Empty Connection"

def login_user(data):
    # data required: email, password
    con = get_connection('Utils/DB/user.db')
    if con !=  None:
        cur = con.cursor()
        query = f"SELECT Password FROM user WHERE Email = \'{data['email']}\';"
        cur.execute(query)
        res = cur.fetchall()
        if(len(res) == 0):
            del con, cur, query, res
            return "Email not exists"
        else:
            db_pwd = res[0][0]
            db_pwd = base64_decoding(db_pwd)
            if db_pwd == data['password']:
                return "Done"
            else:
                return "Wrong password"
    else:
        return "Empty connection"