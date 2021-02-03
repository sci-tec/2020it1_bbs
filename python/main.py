from bottle import route, run, template, request, static_file, redirect
import datetime
import re
import sqlite3
import doData

@route('/static/css/style.css')
def css():
    return static_file('css/style.css', root='./static')

@route("/static/js/app.js")
def js():
    return static_file("/js/app.js", root="./static")

@route('/')
def login():
    return template('python/views/login', text = "", userName = "")

# ログイン
@route('/', method="POST")
def login():
    userId = str(request.forms.userId)
    passWord = str(request.forms.passWord)
    result = doData.checkData(userId, passWord)
    if (result[0]):
        name = result[1]
        redirect('index/{}/{}'.format(name, userId))
    else:
        return template('python/views/login', text = result[1], userName = "")

@route('/signUp')
def signUp():
    return template('python/views/signUp', userId = "")

# 新規登録画面
@route('/signUp', method="POST")
def doSignUp():
    name = str(request.forms.userName)
    passWord = str(request.forms.passWord)

    if (len(name) != 0 and len(passWord) != 0):
        if re.compile("<|>|/").search("{}{}".format(name, passWord)):
            return template('python/views/signUp', userId = '<, >, / は使用不可')
    
        # メインの処理
        userId = doData.createUser(name, passWord)
        print(userId)
        print("name:",name,"\npassWord:", passWord)
        return template('python/views/login', text = '<script>alert("ID: {}")</script>'.format(userId))
    else:
        return template('python/views/signUp', userId = '未入力の欄があります')

@route('/index/<userName>/<userId>')
def index(userName, userId):
    table = "talk"
    url = "{}/{}".format(userName, userId)
    text = doData.getTalk(table)
    return template('python/views/index', text = text, alert = "", userName = userName, url = url)

@route('/index/<userName>/<userId>', method='POST')
def doIndex(userName, userId):
    txt = str(request.forms.message)
    dm = str(request.forms.userId)
    timeNum = ""
    alert = ""
    name = userName
    table = "talk"

    if (len(dm) == len(txt) == 0):
        alert = "文字を入力してください"

    elif (len(dm) > 0 and len(txt) > 0):
        alert = "片側だけ入力して"

    elif (dm == userId):
        alert = "自分"

    # DMの処理
    elif (len(dm) > 0):
        check = doData.checkData(dm, "<>")

        if (check[1] == "パスワードが違う"):
            result = doData.makeTable(userId, dm)[2]

            redirect("/index/{}/{}/{}".format(userName, userId, result))
                        
        else:
            alert = "ユーザーがいない"

    else:

        # 時間を実装する
        for time in range(16):
            timeNum += str(datetime.datetime.now())[time]

        # 使用不可文字の設定
        if re.compile("<|>|/").search(txt):
            alert = "\"<,>,/\"は使用できません。"

        elif (len(txt) == 0):
            alert = "テキストが入力されてない"

        else:
            doData.addChat(table, userName, timeNum, txt)

    text = doData.getTalk(table)
    url = "{}/{}".format(userName, userId)

    return template('python/views/index', text = text, alert = alert, userName = userName, url = url)

@route('/index/<userName>/<userId>/<table>')
def indexDm(userName, userId, table):
    txt = str(request.forms.message)
    dm = str(request.forms.userId)
    timeNum = ""
    alert = ""
    name = userName
    tableName = "_{}_".format(str(table))

    text = doData.getTalk(tableName)
    url = "{}/{}/{}".format(userName, userId, table)

    return template('python/views/index', text = text, alert = alert, userName = userName, url = url)

@route('/index/<userName>/<userId>/<table>', method='POST')
def indexDm(userName, userId, table):
    txt = str(request.forms.message)
    dm = str(request.forms.userId)
    timeNum = ""
    alert = ""
    name = userName
    tableName = "_{}_".format(str(table))

    # 時間を実装する
    for time in range(16):
        timeNum += str(datetime.datetime.now())[time]
    
    # 使用不可文字の設定
    if re.compile("<|>|/").search(txt):
        alert = "\"<,>,/\"は使用できません。"
    elif (len(txt) == 0):
        alert = "テキストが入力されてない"
    else:
        doData.addChat(tableName , userName, timeNum, txt)

    text = doData.getTalk(tableName)
    url = "{}/{}/{}".format(userName, userId, table)

    return template('python/views/index', text = text, alert = alert, userName = userName, url = url)

run(host='localhost', port=8080, debug=True)