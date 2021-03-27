import sqlite3
from sqlite3 import Error

def get_connection(db_name):
	try:
		con = sqlite3.connect(db_name)
	except Error:
		con = None
		print(Error)
	return con

def get_table_details(db_name):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';")
    for item in cursor.fetchall():
        prop = item[0].replace("CREATE TABLE", "").replace("(", "\n  ").replace(")", "")
        prop = prop.replace(",","\n ")
        print(f"properties of => {prop}")
    print("="*20)
    del con, cursor, prop

def make_user_table():
    con = get_connection('user.db')
    cursorObj = con.cursor()
    query = ('CREATE TABLE IF NOT EXISTS user ('+
        'ID TEXT PRIMARY KEY, '+
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

if __name__ == '__main__':
    print("Database Manager")
    print("="*20)
    make_user_table()
    view_user_table()
    get_table_details('user.db')