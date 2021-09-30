from os import truncate
import uuid
import sqlite3
from sqlite3 import Error
from Data.zHashing import encode, decode
user_db_path = 'Data/user.db'

def get_connection(db_name):
	try:
		con = sqlite3.connect(db_name)
	except Error:
		con = None
		print(Error)
	return con

def register_user(data):
    # data required: firstName, lastName, email, phoneNumber, password
    print("Registering new user")
    con = get_connection(user_db_path)
    if con != None:
        cur = con.cursor()
        try:
            em = data['email']
        except:
            return "Email Cannot Be Empty", False
        query = f"SELECT Email FROM user WHERE Email = \'{em}\';"
        cur.execute(query)
        if len(cur.fetchall()) != 0:
            return "Email Already Exists", False
        
        try:
            pn = data['phoneNumber']
        except:
            return "Phone Number Cannot Be Empty", False
        query = f'SELECT PhoneNumber FROM user WHERE PhoneNumber = \'{pn}\';'
        if len(cur.fetchall()) != 0:
            return "Phone Number Already Exists ", False

        new_id = str(uuid.uuid1())
        try:
            entities = (new_id, data['firstName'],
                data['lastName'], data['email'],
                data['phoneNumber'], 
                encode(data['password']),
                0, "")
        except:
            return "Parameter / Payload Error", False

        query = "INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, entities)
        con.commit()
        del data, con, cur, new_id, entities, query
        return "Register Success", True
    else:
        return "Empty Connection", False

def login_user(data):
    # data required: email, password
    con = get_connection(user_db_path)
    if con !=  None:
        cur = con.cursor()
        query = f"SELECT Password, IsConsultant, UserId, FirstName, LastName, Email, PhoneNumber FROM user WHERE Email = \'{data['email']}\';"
        cur.execute(query)
        res = cur.fetchall()
        print(res)
        if(len(res) == 0):
            del con, cur, query, res
            return "Email not exists", 0, "No Id", "No Name", data['email'], "No Number", False
        else:
            db_pwd = res[0][0]
            db_pwd = decode(db_pwd)
            del con, cur, query
            if db_pwd == data['password']:
                return "Logged In", res[0], True
            else:
                return "Wrong password", None, False
    else:
        return "Empty connection", None, False