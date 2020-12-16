from bottle import route, run, template, request, static_file
import fileUtil
import datetime
import re

@route('/bbs/css/style.css')
def css():
    return static_file('./css/style.css', root='.')

@route("/bbs/js/app.js")
def js():
    return static_file("./js/app.js", root=".")

@route('/bbs')
def bulletin():
    currentList = fileUtil.readFile("sample.txt")
    return template('index', text = currentList, alert = "")

@route('/bbs', method='POST')
def do_hello():
    name = request.forms.name
    txt = request.forms.message
    timeNum = ""
    warningText = ""

    # 時間を実装する
    for time in range(16):
        timeNum += str(datetime.datetime.now())[time]

    # 使用不可文字の設定
    if re.compile("<|>|/").search("{}{}".format(name, txt)):
        warningText = "\"<,>,/\"は使用できません。"

    else:
        # 削除コマンドの実装
        if len(name) == 2 and "削除" in name:
            fileUtil.writeFile("sample.txt", "")

        # nameが空欄時 の処理
        elif len(name) == 0:
            name = "名無しさん"

        # messageが空欄時の処理
        elif len(txt) == 0:
            warningText = "messageに文字を入力して下さい"

        if len(txt) != 0:
            newText = "NAME: " + name + '<br>' + "TIME: " + "{}".format(timeNum) + "<br>" + "TEXT: " + txt + "<br><br>"
            fileUtil.addNewLine("sample.txt", newText)

    newList = fileUtil.readFile("sample.txt")
    return template('index', text=newList, alert=warningText)

run(host='localhost', port=8080, debug=True)