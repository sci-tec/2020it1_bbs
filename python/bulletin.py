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
        warningText = "alert('\"<,>,/\"は使用できません。');"

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
                    newText = "NAME: BOT{}<br>TIME:{}<br>TEXT: へろ～～～<br><br>".format(times + 1, timeNum)
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
                warningText = ""

            # messageだけ空欄時
            else:
                warningText = "alert('messageに文字を入力して下さい');"

    newList = fileUtil.readFile("sample.txt")
    warningText = "<script>{}</script>".format(warningText)

    return template('index', text=newList, alert=warningText)

run(host='localhost', port=8080, debug=True)