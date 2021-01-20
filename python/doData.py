from createId import createId
import re
import sqlite3

# 新規追加
def createUser(name, password):
    dbname = "USER.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    userId = createId()
    cur.execute("INSERT INTO user(userId, name, pass) values('{}', '{}', '{}')".format(userId, name, password))
    print(userId)

    return userId

    conn.commit()
    cur.close()
    conn.close()


# ログイン
def login(userId, password):
    dbname = "USER.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM user where userId == "{}"'.format(userId))
    data = cur.fetchall()
    print(data)
    if (len(data) == 1):
        if (data[0][2] == password):
            print("{},ログイン".format(data[0][1]))
        else:
            print("パスワードが違う")
    else:
        print ("ユーザーがいない")
    
    conn.commit()
    cur.close()
    conn.close()

# 削除
def deliteUser(userId, password):
    dbname = "USER.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    cur.execute('SELECT * FROM user where userId == "{}"'.format(userId))
    data = cur.fetchall()
    print(data)
    if (len(data) == 1):
        if (data[0][2] == password):
            print("{},削除".format(data[0][1]))
            cur.execute('DELETE FROM user where userId == "{}"'.format(userId))
        else:
            print("パスワードが違う")
    else:
        print ("ユーザーがいない")

    conn.commit()
    cur.close()
    conn.close()