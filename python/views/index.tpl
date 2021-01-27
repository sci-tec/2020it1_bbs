<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="bbs/css/style.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bulletin board</title>
</head>

<body>
    <div id="scrollInner" class="wrapper">

        {{!text}}

        {{!alert}}
        <div id="postArea">
            <form method="post" action="/index/{{userName}}">
                <div class="clearfix">
                    <div id="form">
                        <ul>
                            <input type="text" id="name" name="name" placeholder="name">
                        </ul>
                        <ul>
                            <input type="text" id="message" name="message" placeholder="message">
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