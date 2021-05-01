import sqlite3
from sqlite3 import Error
from Data.zHashing import *
user_db_path = 'Data/user.db'
consultant_details_db_path = 'Data/consultant_details.db'

def get_connection(db_name):
	try:
		con = sqlite3.connect(db_name)
	except Error:
		con = None
		print(Error)
	return con

def register_consultant(data):
    # data required: email, phoneNumber, password
    # also: bio, experience, honor, education, rating(float)
    con = get_connection(user_db_path)
    if con != None:
        cur = con.cursor()
        query = 'UPDATE user SET IsConsultant = 1 WHERE email = ? AND PhoneNumber = ? AND Password = ?'
        try:
            entities = (data['email'], data['phoneNumber'], encode(data['password']))
            bio, exp = data['bio'], data['experience']
            honor, education, rating = data['honor'], data['education'], data['rating']
        except:
            return "Data is not well supllied"
        cur.execute(query, entities)
        con.commit()
        query = 'SELECT UserId FROM user WHERE email = ? AND PhoneNumber = ? AND Password = ?'
        cur.execute(query, entities)
        userId = cur.fetchone()[0]
    else:
        return "Empty Connection"
    con = get_connection(consultant_details_db_path)
    if con != None:
        cur = con.cursor()
        query = "INSERT INTO consultant_details VALUES(?, ?, ?, ?, ?, ?)"
        entity = (userId, bio, exp, honor, education, rating)
        cur.execute(query, entity)
        con.commit()
        return "Done"
    else:
        return "Empty Connection"
    
def getall_consultant():
    # no data required
    con = get_connection(user_db_path)
    if con != None:
        cur = con.cursor()
        query = "SELECT UserId, FirstName, LastName, Email, PhoneNumber FROM user WHERE IsConsultant = 1"
        cur.execute(query)
        ret = []
        for i in cur.fetchall():
            ret.append('ID:' + i[0] + '->' + i[1] + ' ' + i[2] + '|' + i[3] + '|' + i[4])
        del cur, con, query
        return ret
    else:
        return "Empty Connection"

def get_consultant_details(data):
    # data required: userId
    con = get_connection(consultant_details_db_path)
    if con != None:
        cur = con.cursor()
        query = "SELECT * FROM consultant_details WHERE UserId = ?"
        try:
            entity = (data['userId'],)
        except:
            return "Data is not well supplied"
        cur.execute(query, entity)
        ret = cur.fetchone()
        dictret = {
            "userId":ret[0],
            "bio":ret[1],
            "experience":ret[2],
            "honor":ret[3],
            "education":ret[4],
            "rating":ret[5]
        }
        return dictret
    else:
        return "Empty Connection"