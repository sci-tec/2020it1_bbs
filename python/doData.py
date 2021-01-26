from createId import createId
import fileUtil
import re

# テキストデータを辞書データに変換
def getDict():
    datas = fileUtil.readFile("data.txt")
    datas = datas.split("_")
    dataBase = {}
    for data in datas:
        try:
            rawData = data.split("/")
            dataBase["{}".format(rawData[0])] = ["{}".format(rawData[1]), "{}".format(rawData[2])]
        except IndexError:
            return dataBase

# パスワードとIDを照合する
def checkData(userId, passWord):
    datas = getDict()
    
    try:
        if (datas[userId][1] == "{}".format(passWord)):
            return [True, datas[userId][0]]
        else:
            return [False, "パスワードが違う"]
    except KeyError:
        return [False, "ユーザーがいない"]

# 新規追加
def createUser(name, passWord):
    userId = createId()
    fileUtil.addNewData("data.txt", "{}/{}/{}_".format(userId, name, passWord))
    return userId

# ログイン
def login(userId, passWord):
    data = checkData(userId, passWord)
    if (data[0]):
        return "{}, ログイン".format(data[1])
    else:
        return data[1]

# 削除
def deliteUser(userId, passWord):
    setDict = getDict()
    datas = checkData(userId, passWord)
    if (datas[0]):
        return "{}, 削除".format(datas[1])
        setDict.pop("{}".format(userId))
        newData = ""
        for data in setDict:
            for key in setDict.keys():
                strKey = str(key)
                newData += "{}/{}/{}_".format(strKey, setDict[strKey][0], setDict[strKey][1])
        fileUtil.writeFile("data.txt", newData)
    else:
        return datas[1]