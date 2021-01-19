from createId import createId
from data import dataBase
import fileUtil
import re

# ファイルへの書き込み
def dataUpdate(data):
    fileUtil.writeFile("python/data.py","def dataBase():\n")
    fileUtil.addNewLineNotag("python/data.py", "    data = {}\n".format(data))
    fileUtil.addNewLineNotag("python/data.py", "    return data")

# 新規追加
def createUser(name, password):
    if re.compile("\"|\'|%|:|;|\|_|#|@|~|-|=|!").search("{}{}".format(name, password)):
        print("使えない","{}{}".format(name, password))
    else:
        userId = createId(5)
        print(userId)
        data = dataBase()
        newData = {userId: [name, password]}
        data.update(newData)
        dataUpdate(data)
        return userId

# ログイン
def login(userId, password):
    data = dataBase()
    try:
        if (data[userId][1] == password):
            print("{},ログイン".format(data[userId][0]))
        else:
            print("パスワードが違う")
    except KeyError:
        print ("ユーザーがいない")

# 削除
def clear(userId, password):
    data = dataBase()
    try:
        if (data[userId][1] == password):
            data.pop(userId)
            print("削除")
            dataUpdate(data)
        else:
            print("パスワードが違う")
    except KeyError:
        print ("ユーザーがいない")

createUser("name", "pass")