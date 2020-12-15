def readFile(filename):
    open_file = open(filename, encoding = "utf-8")
    raw_data = open_file.read()
    open_file.close()
    return raw_data

def writeFile(filename, data):
    output_file = open(filename, 'w', encoding = "utf-8")
    text = data
    output_file.write(text)
    output_file.close()

def addNewLine(filename, data):
    try:
        raw_data = readFile(filename)
    except Exception as e:
        raw_data = ""
    raw_data += data + '<br>'
    writeFile(filename, raw_data)