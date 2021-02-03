<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/css/style.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bulletin board</title>
</head>

<body>
    <div id="scrollInner" class="wrapper">
        <h3>＜{{userName}}＞</h3>
        {{!text}}

        {{!alert}}
        <div id="postArea">
            <form method="post" action="/index/{{url}}">
                <div class="clearfix">
                    <div id="form">
                        <ul>
                            <input type="text" id="message" name="message" placeholder="メッセージ">
                            <input type="text" id="userId" name="userId" placeholder="ユーザーID">
                        </ul>
                    </div>
                    <input type="submit" id="post" value="POST">
                </div>
            </form>
        </div>
        <br>
        <script src="https://code.jquery.com/jquery-2.2.4.min.js"></script>
        <script type="text/javascript" src="bbs/js/app.js"></script>
    </div>
</body>
</html>