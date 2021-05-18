import uuid
import sqlite3
from sqlite3 import Error
import time
from datetime import datetime
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
        query_check = "select Chatid from chat_header where \
            (UserId1=? and UserId2=?) or (Userid1=? and UserId2=?)"
        entities = (sender, receiver, receiver, sender)
        cur.execute(query_check, entities)
        data = cur.fetchall()
        if len(data) > 0:
            return data[0][0], True
        newid = str(uuid.uuid1())
        query = "insert into chat_header values(?, ?, ?)"
        entities = (newid, sender, receiver)
        cur.execute(query, entities)
        con2.commit()
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
            query = "select FirstName, LastName from user\
                where UserId = ?"
            entities = (friendid,)
            cur1.execute(query, entities)
            user_db_res = cur1.fetchall()
            print(user_db_path)
            friendname = user_db_res[0][0] + ' ' + user_db_res[0][1]
            temp = {
                "chatId" : i[0],
                "friendId" : friendid,
                "friendNamme" : friendname
            }
            returnlist.append(temp)
        return returnlist, True
    else:
        return "empty connection", False
    
def sendchat(data):
    try:
        userid = data['userId']
        chatid = data['chatId']
        message = data['message']
    except:
        return "userId, chatId, or message not specified", False
    con = get_connection(chat_details_db_path)
    if con != None:
        cur = con.cursor()
        ts =  int(time.time())
        query = "insert into chat_details values(?, ?, ?, ?)"
        params = (chatid, userid, message, ts)
        try:
            cur.execute(query, params)
            con.commit()
        except:
            return "failed to send chat", False
        return "message sent", True
    else:
        return "empty connection", False

def getchatdetails(data):
    try:
        chatid = data['chatId']
        userid = data['userId']
    except:
        return "chatId or userId not specified", False
    con = get_connection(chat_details_db_path)
    if con != None:
        cur = con.cursor()
        ts =  int(time.time())
        query = "select * from chat_details where ChatId = ? order by TimeStamp DESC"
        params = (chatid,)
        retlist = []
        try:
            cur.execute(query, params)
            datalist = cur.fetchall()
            for i in datalist:
                sender = 0
                if i[1] == userid:
                    sender = 1
                else:
                    sender = 0
                temp = {
                    'message' : str(i[2]),
                    "time" : str(datetime.fromtimestamp(int(i[3]))),
                    "isSender" : sender
                }
                retlist.append(temp)
        except:
            return "failed to get chats", False
        return retlist, True
    else:
        return "empty connection", False