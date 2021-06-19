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
            ChatId TEXT PRIMARY KEY, UserId1 TEXT,\
            UserId2 TEXT) " 
        cur.execute(query)
        con.commit()
    
def make_chat_details_table():
    with get_connection('chat_details.db') as con:
        cur = con.cursor()
        query = "create table if not exists chat_details(\
            ChatId TEXT, SenderId TEXT, Message TEXT, TimeStamp TEXT)"
        cur.execute(query)
        con.commit()

def insert_dummies():
    with get_connection('user.db') as con:
        cur = con.cursor()
        query = "insert into user values(?,?,?,?,?,?,?,?)"
        entities = ('3d9b3ea6-ac8f-11eb-9530-9557126e83fc','admin','','admin@gmail.com','081233445566','YWRtaW4=',1,'') #adminpwd
        cur.execute(query, entities)
        entities = ('c69f9186-d0fa-11eb-84c8-569e2975b3f6','Wiliam','Tannuwijaya','081233439566', 'william@gmail.com','d2lsbGlhbQ==', 1, '') #william
        cur.execute(query, entities)
        entities = ('f0eb5bce-d0f4-11eb-84c8-569e2975b3f6', 'Brian Karnadi', 'Japar','081233445216', 'brian@gmail.com', 'YnJpYW4=', 1, '') #brian
        cur.execute(query, entities)
        entities = ('f0eb543e-dbfs-1s2b-84cv-5fs32975b3f6', 'Cornelius', 'Tantius','081237285566', 'cornel@gmail.com', 'Y29ybmVs', 1, '') #cornel
        cur.execute(query, entities)
        entities = ('f0eb5fje-34ns-11sb-82cv-5fs32j34g3f6', 'Ricky', '','081247444362', 'ricky@gmail.com', 'cmlja3k=', 1, '') #ricky
        cur.execute(query, entities)
        con.commit()

    with get_connection('consultant_details.db') as con:
        cur = con.cursor()
        query = "insert into consultant_details values(?, ?, ?, ?, ?, ?)"
        bio = 'This is biography panel, this panel will describe this user\'s biography in short. Biography allows user to know deeper about this consultant and decide wether he is about to consult with this consultant or not.'
        exp = 'This consultant will share his experience of work and everything he has done to make sure the user decide this is the correct consultant.'
        honor = 'This will show the all the honor and achievement that current consultant has achieved.\n- Achievement 1,\n- Achievement 2\n- Honor 1'
        edu = 'Education that current consultant has gone through:\n- Elementary school\n- High school\n- University 1\n- University 2'
        entities = ('3d9b3ea6-ac8f-11eb-9530-9557126e83fc', bio, exp, honor, edu, 4.7)
        cur.execute(query, entities)
        entities = ('c69f9186-d0fa-11eb-84c8-569e2975b3f6', bio, exp, honor, edu, 4.7)
        cur.execute(query, entities)
        entities = ('f0eb5bce-d0f4-11eb-84c8-569e2975b3f6', bio, exp, honor, edu, 4.7)
        cur.execute(query, entities)
        entities = ('f0eb543e-dbfs-1s2b-84cv-5fs32975b3f6', bio, exp, honor, edu, 4.7)
        cur.execute(query, entities)
        entities = ('f0eb5fje-34ns-11sb-82cv-5fs32j34g3f6', bio, exp, honor, edu, 4.7)
        cur.execute(query, entities)
        con.commit()

if __name__ == '__main__':
    print("Database Manager")
    print("="*20)
    make_user_table()
    make_consultant_details_table()

    make_chat_header_table()
    make_chat_details_table()

    insert_dummies()
    view_user_table()
