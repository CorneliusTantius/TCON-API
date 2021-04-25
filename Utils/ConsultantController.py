import sqlite3
from sqlite3 import Error
from Data.Hashing import *
user_db_path = 'Data/user.db'

def get_connection(db_name):
	try:
		con = sqlite3.connect(db_name)
	except Error:
		con = None
		print(Error)
	return con

def register_consultant(data):
    # data required: email, phoneNumber, password
    con = get_connection(user_db_path)
    if con != None:
        cur = con.cursor()
        query = 'UPDATE user SET IsConsultant = 1 WHERE email = ? AND PhoneNumber = ? AND Password = ?'
        try:
            entities = (data['email'], data['phoneNumber'], encode(data['password']))
        except:
            return "Data is not well supllied"
        cur.execute(query, entities)
        con.commit()
        return "Done"
    else:
        return "Empty Connection"

def getall_consultant():
    # no data required
    con = get_connection(user_db_path)
    if con != None:
        cur = con.cursor()
        query = "SELECT ID, FirstName, LastName, Email, PhoneNumber FROM user WHERE IsConsultant = 1"
        cur.execute(query)
        ret = []
        for i in cur.fetchall():
            ret.append('ID:' + i[0] + '->' + i[1] + ' ' + i[2] + '|' + i[3] + '|' + i[4])
        del cur, con, query
        return ret
    else:
        return "Empty Connection"
def get_consultant_details(data):
    return