from bottle import route, run, template, request, static_file
import fileUtil
import datetime

@route('/bbs/css/style.css')
def css():
    return static_file('./css/style.css', root='.')

@route("/bbs/js/app.js")
def js():
    return static_file("./js/app.js", root=".")

@route('/bbs')
def bulletin():
    currentList = fileUtil.readFile("sample.txt")

    return template('index', text = currentList)

@route('/bbs', method='POST')
def do_hello():
    name = request.forms.name
    txt = request.forms.message
    timeNum = ""

    if len(name) == 2 and name[0] == "削" and name[1] == "除":
        fileUtil.writeFile("sample.txt", "")

    if len(name) == 0:
        name = "名無しさん"

    for time in range(16):
        timeNum += str(datetime.datetime.now())[time]

    if len(txt) != 0:
        newText = "NAME: " + name + '<br>' + "TIME: " + "{}".format(timeNum) + "<br>" + "TEXT: " + txt + "<br><br>"
        fileUtil.addNewLine("sample.txt", newText)

    newList = fileUtil.readFile("sample.txt")

    return template('index', text=newList)

run(host='localhost', port=8080, debug=True)