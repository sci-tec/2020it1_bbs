<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/static/css/style.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>新規登録画面</title>
</head>

<body>
    <div id="wrapper">
        <div id="form">
            <h1>新規登録</h1>
            <form method="post" action="/signUp">
                <div id="input">
                    <input type="text" id="userName" name="userName" placeholder="ユーザーネーム">
                    <br>
                    <input type="password" id="passWord" name="passWord1" placeholder="パスワード">
                    <br>
                    <input type="password" id="passWord" name="passWord2" placeholder="パスワード（確認用）">
                    <br>
                    <input type="submit" onclick="location.href='/'" id="post" value="新規登録">
                    <a href="/" id="url">前に戻る</a>
                </div>
            </form>
        </div>
    </div>

    <div id="alert">
        {{!userId}}
    </div>

</body>

</html>