from createId import createId
import re
import sqlite3

# データベースの中身を確認
def showData():
    dbname = "python/USER.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('SELECT * FROM user')
    print(cur.fetchall())

    conn.commit()
    cur.close()
    conn.close()

# データベースからデータを取り出す
def getData():
    dbname = "python/USER.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('SELECT * FROM user')
    datas = cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()

    return datas

# データベースを辞書データに変換
def getDict():
    datas = getData()
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
    userId = createId()
    cur.execute("INSERT INTO user(userId, name, pass) values('{}', '{}', '{}')".format(userId, name, passWord))
    print(userId)

    conn.commit()
    cur.close()
    conn.close()

    return userId

# ログイン
def login(userId, passWord):
    result = checkData(userId, passWord)

    if (result[0]):
        return "{}, ログイン".format(result[1])
    else:
        return result[1]

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