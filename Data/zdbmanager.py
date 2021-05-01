import sqlite3
from sqlite3 import Error

def get_connection(db_name):
	try:
		con = sqlite3.connect(db_name)
	except Error:
		con = None
		print(Error)
	return con

def make_user_table():
    con = get_connection('user.db')
    cursorObj = con.cursor()
    query = ('CREATE TABLE IF NOT EXISTS user ('+
        'UserId TEXT PRIMARY KEY, '+
        'FirstName TEXT, LastName TEXT, Email TEXT, ' +
        'PhoneNumber TEXT, Password TEXT, ' + 
        'IsConsultant INTEGER, Url TEXT)')
    cursorObj.execute(query)
    con.commit()
    del con, cursorObj, query

def view_user_table():
    con = get_connection('user.db')
    cursorObj = con.cursor()
    query = 'SELECT * FROM user'
    cursorObj.execute(query)
    data = cursorObj.fetchall()
    for item in data:
        print(item)
    del con, cursorObj, query, data

def make_consultant_details_table():
    with get_connection('consultant_details.db') as con:
        cursorObj = con.cursor()
        query = " CREATE TABLE IF NOT EXISTS consultant_details (\
            UserId TEXT PRIMARY KEY, Bio TEXT, Experience TEXT, \
            Honor TEXT, Education TEXT, Rating FLOAT)"
        cursorObj.execute(query)
        con.commit()

def make_chat_header_table():
    with get_connection('chat_header.db') as con:
        cur = con.cursor()
        query = "CREATE TABLE IF NOT EXISTS chat_header (\
            ChatId TEXT PRIMARY KEY, UserId1 TEXT\
            UserId2 TEXT) " 
        cur.execute(query)
        con.commit()

def insert_dummies():
    with get_connection('user.db') as con:
        cur = con.cursor()
        query = "insert into user values(?,?,?,?,?,?,?,?)"
        entities = ('admin','admin','','admin@gmail.com','081233445566','YWRtaW4=',1,'')
        cur.execute(query, entities)
        con.commit()

if __name__ == '__main__':
    print("Database Manager")
    print("="*20)
    make_user_table()
    make_consultant_details_table()
    make_chat_header_table()
    # insert_dummies()
    view_user_table()
