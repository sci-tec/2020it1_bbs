from bottle import route, run, template, request, static_file, redirect
from createId import createId
import fileUtil
import datetime
import re
import sqlite3
import doData

dbname = "python/USER.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

@route('/bbs/css/style.css')
def css():
    return static_file('./public/css/style.css', root='.')

@route("/bbs/js/app.js")
def js():
    return static_file("./public//js/app.js", root=".")

@route('/')
def login():
    return template('python/views/login', text = "", userName = "")

# ログイン処理
@route('/', method="POST")
def login():
    userId = str(request.forms.userId)
    passWord = str(request.forms.passWord)
    result = doData.checkData(userId, passWord)
    if (result[0]):
        name = result[1]
        text = fileUtil.readFile("python/sample.txt")
        redirect('index/{}'.format(name))
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
        if re.compile("<|>|/|_").search("{}{}".format(name, passWord)):
            return template('python/views/signUp', userId = '<, >, /, _, は使用不可')
        # メインの処理
        userId = createId()
        doData.createUser(name, passWord)
        print(userId)
        print("name:",name,"\npassWord:", passWord)
        return template('python/views/login', text = '<script>alert("ID: {}")</script>'.format(userId))
    else:
        return template('python/views/signUp', userId = '未入力の欄があります')

@route('/index/<userName>')
def bulletin(userName):
    currentList = fileUtil.readFile("python/sample.txt")
    return template('python/views/index', text = currentList, alert = "", userName = userName)

@route('/index/<userName>', method='POST')
def do_hello(userName):
    txt = str(request.forms.message)
    timeNum = ""
    alert = ""
    name = userName
    # 時間を実装する
    for time in range(16):
        timeNum += str(datetime.datetime.now())[time]

    # 使用不可文字の設定
    if re.compile("<|>|/").search(txt):
        alert = "alert('\"<,>,/\"は使用できません。');"

    newText = "NAME: {}<br>TIME: {}<br>TEXT: {}<br><br>".format(name, timeNum, txt)
    fileUtil.addNewLine("python/sample.txt", newText)
    text = fileUtil.readFile("python/sample.txt")
    alert = "<script>{}</script>".format(alert)

    return template('python/views/index', text=text, alert=alert, userName = userName)

run(host='localhost', port=8080, debug=True)