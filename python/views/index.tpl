<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/static/css/index.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bulletin board</title>
</head>

<body>
    <div id="scrollInner" class="wrapper">
        <h3>＜{{userName}}＞</h3>
        {{!text}}

        <div id="alert">
            {{!alert}}
        </div>

        <div id="wrapper">

            <form method="post" action="/index/{{url}}">

                <div id="input">
                    <div class="clearfix">

                        <div id="dmForm">
                            
                            <input type="text" id="userId" name="userId" placeholder="ユーザーID">
                        </div>

                        <input type="text" id="message" name="message" placeholder="メッセージ">
                        <input type="submit" id="post" value="POST">

                    </div>
                </div>
            </form>

        </div>
        <br>
        <script src="https://code.jquery.com/jquery-2.2.4.min.js"></script>
        <script type="text/javascript" src="/static/js/app.js"></script>
    </div>
</body>

</html>