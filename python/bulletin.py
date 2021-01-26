from bottle import route, run, template, request, static_file
from createId import createId
import fileUtil
import datetime
import re
import sqlite3
import doData

dbname = "USER.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

@route('/bbs/css/style.css')
def css():
    return static_file('./css/style.css', root='.')

@route("/bbs/js/app.js")
def js():
    return static_file("./js/app.js", root=".")

@route('/login.html')
def login():
    return template('login', text = "")

@route('/login.html', method="新規登録")
def doLogin():
    return template('signUp', userId = "")

# ログイン処理
@route('/login.html', method="POST")
def login():
    userId = str(request.forms.userId)
    passWord = str(request.forms.passWord)
    result = doData.checkData(userId, passWord)
    if (result[0]):
        return template('index', text = "{}, ログイン".format(result[1]), alert = "")
    else:
        return template('login', text = result[1])

@route('/signUp.html')
def signUp():
    return template('signUp', userId = "")

# 新規登録画面
@route('/signUp.html', method="POST")
def doSignUp():
    name = str(request.forms.userName)
    passWord = str(request.forms.passWord)

    if (len(name) != 0 and len(passWord) != 0):
        if re.compile("<|>|/|_").search("{}{}".format(name, passWord)):
            return template('signUp', userId = '<, >, /, _, は使用不可')
        # メインの処理
        userId = createId()
        doData.createUser(name, passWord)
        print(userId)
        print("name:",name,"\npassWord:", passWord)
        return template('login', text = '<script>alert("ID: {}")</script>'.format(userId))
    else:
        return template('signUp', userId = '未入力の欄があります')

@route('/index.html')
def bulletin():
    currentList = fileUtil.readFile("sample.txt")
    return template('index', text = currentList, alert = "")

@route('/index.html', method='POST')
def do_hello():
    name = request.forms.name
    txt = request.forms.message
    timeNum = ""
    alert = ""

    # 時間を実装する
    for time in range(16):
        timeNum += str(datetime.datetime.now())[time]

    # 使用不可文字の設定
    if re.compile("<|>|/").search("{}{}".format(name, txt)):
        alert = "alert('\"<,>,/\"は使用できません。');"

    else:
        # コマンド群
        if len(name) != 0 and name[0] == "@":

            # 削除
            if re.compile("ki11").search(name):
                fileUtil.writeFile("sample.txt", "")

            # 自動投稿
            elif re.compile("cr8").search(name):
                if re.compile(":").search(name):
                    command, number = name.split(':')
                    timesNum = int(number)

                for times in range(timesNum):
                    newText = "NAME: 中本BOT{}<br>TIME:{}<br>TEXT: 蒙古タンメン<br><br>".format(times + 1, timeNum)
                    fileUtil.addNewLine("sample.txt", newText)

        if len(txt) != 0:
            # nameが空欄時 の処理
            if len(name) == 0:
                name = "名無しさん"

            newText = "NAME: " + name + '<br>' + "TIME: " + "{}".format(timeNum) + "<br>" + "TEXT: " + txt + "<br><br>"
            fileUtil.addNewLine("sample.txt", newText)

        else:
            # すべて空欄時
            if len(name) == 0 or name[0] == "@":
                alert = ""

            # messageだけ空欄時
            else:
                alert = "alert('messageに文字を入力して下さい');"

    text = fileUtil.readFile("sample.txt")
    alert = "<script>{}</script>".format(alert)

    return template('index', text=text, alert=alert)

run(host='localhost', port=8080, debug=True)