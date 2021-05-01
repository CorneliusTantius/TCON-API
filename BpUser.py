import sqlite3
from sqlite3 import Error
user_db_path = 'Data/user.db'

def getuid_dev(data):
    # email required
    con = get_connection(user_db_path)
    if con != None:
        cur = con.cursor()
        try:
            e = data['email']
        except:
            return "Email not Supplied"
        query = f"SELECT FirstName, LastName, Email, ID FROM user WHERE email = \'{e}\'"
        cur.execute(query)
        ret = []
        for i in cur.fetchall():
            ret.append(i[0] + ' ' + i[1] + '|' + i[2] + '|' + i[3])
        del cur, con, query
        return ret
    else:
        return "Empty Connection"