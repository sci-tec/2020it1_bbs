import sqlite3
import string
import secrets
import re

# IDを作る
def getId():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return "".join(secrets.choice(chars) for x in range(12))

# データベースからデータを取り出す
def getData(table):
    dbname = "python/USER.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('SELECT * FROM {}'.format(table))
    datas = cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()

    return datas

# データの中身を確認
def showData(table):
    dbname = "python/USER.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('SELECT * FROM {}'.format(table))
    print(cur.fetchall())

    conn.commit()
    cur.close()
    conn.close()

# データベースを辞書データに変換
def getDict():
    datas = getData("user")
    dataDict = {}

    for data in datas:
        dataDict[data[0]] = [str(data[1]), str(data[2])]

    return dataDict

# パスワードとIDを照合
def checkData(userId, passWord):
    dataDict = getDict()

    try:
        if (dataDict[userId][1] == passWord):
            return [True, dataDict[userId][0]]
        else:
            return [False, "パスワードが違う"]
    except KeyError:
        return [False, "ユーザーがいない"]

# 新規追加
def createUser(name, passWord):
    dbname = "python/USER.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    userId = getId()
    cur.execute("INSERT INTO user(userId, name, pass) values('{}', '{}', '{}')".format(userId, name, passWord))

    conn.commit()
    cur.close()
    conn.close()

    return userId

# 削除
def deleteUser(userId, passWord):
    dbname = "python/USER.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('SELECT * FROM user where userId == "{}"'.format(userId))
    data = cur.fetchall()

    if (result[0]):
        return "{}, 削除".format(result[1])
        cur.execute('DELETE FROM user where userId == "{}"'.format(userId))
    else:
        return result[1]

    conn.commit()
    cur.close()
    conn.close()

# talkの情報を追加
def addChat(table, name, time, text):
    dbname = "python/USER.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("INSERT INTO {}(name, time, text) values('{}', '{}', '{}')".format(table, name, time, text))

    conn.commit()
    cur.close()
    conn.close()

# talkデータをタイムライン風に変換
def getTalk(table):
    chat = ""
    datas = getData(table)

    for data in datas:
        chat += "NAME: {}<br>TIME: {}<br>TEXT: {}<br><br>".format(data[0], data[1], data[2])

    return chat

# 新しいテーブルを制作,既存のものがあれば何もしない
def makeTable(userId1, userId2):
    dbname = "python/USER.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    id1 = userId1
    id2 = userId2

    if (userId1 < userId2):
        id1, id2 = userId2, userId1

    idName = "{}{}".format(id1, id2)
    
    try:
        cur.execute('create table _{}_(name, time, text)'.format(idName))

        return [True, "作成", idName]
    except sqlite3.OperationalError:

        return [False, "既存", idName]
    
    conn.commit()
    cur.close()
    conn.close()