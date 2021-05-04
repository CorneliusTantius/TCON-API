import uuid
import sqlite3
from sqlite3 import Error
user_db_path = 'Data/user.db'
chat_header_db_path = 'Data/chat_header.db'
chat_details_db_path = 'Data/chat_details.db'

def get_connection(db_name):
	try:
		con = sqlite3.connect(db_name)
	except Error:
		con = None
		print(Error)
	return con

def create_new_chat(data):
    con2 = get_connection(chat_header_db_path)
    if con2 != None:
        try:
            sender, receiver = data['sender'], data['receiver']
        except:
            return "data is not supplied", False
        cur = con2.cursor()
        query_check = "select TOP 1 ChatId from chat_header where \
            (UserId1=? and UserId2=?) or (Userid1=? and UserId2=?)"
        entities = (sender, receiver, receiver, sender)
        cur.execute(query_check, entities)
        if len(cur.fetchall()) > 0:
            return cur.fetchall()[0]
        newid = str(uuid.uuid1())
        query = "insert into chat_header values(?, ?, ?)"
        entities = (newid, sender, receiver)
        cur.execute(query, entities)
        return newid, True
    else:
        return "empty connection", False

def get_all_chat_header(data):
    con1 = get_connection(user_db_path)
    con2 = get_connection(chat_header_db_path)
    if con1!=None and con2!=None:
        try:
            userid = data['userId']
        except:
            return "userId is not supplied", False
        cur = con2.cursor()
        query = "select * from chat_header where\
            UserId1 = ? or UserId2 = ?"
        entities = (userid, userid)
        cur.execute(query, entities)
        datalist = cur.fetchall()
        returnlist = []
        for i in datalist:
            if i[1] == userid:
                friendid = i[2]
            else:
                friendid = i[1]
            cur1 = con1.cursor()
            query = "select top 1 FirstName, LastName from user\
                where UserId = ?"
            entities = (friendid,)
            cur1.execute(query, entities)
            friendname = cur1.fetchall()[0][0] + ' ' + cur1.fetchall()[0][1]
            temp = {
                chatId : i[0],
                friendId : friendid,
                friendNamme : friendname
            }
            returnlist.append(temp)
        return returnlist, True
    else:
        return "empty connection", False