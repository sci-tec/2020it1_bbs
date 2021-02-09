<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/static/css/style.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ログインページ</title>
</head>

<body>
    <div id="wrapper">
        <div id="form">
            <h1>ログイン</h1>
            <form method="post" action="/">
                <div id="input">
                    <input type="text" id="userId" name="userId" placeholder="ユーザーID">
                    <br>
                    <input type="password" id="passWord" name="passWord" placeholder="パスワード">
                    <br>
                    <input type="submit" onclick="location.href='index'" id="post" value="ログイン">
                    <a href="signUp" id="url">新規登録はこちら</a>
                </div>
            </form>
        </div>
    </div>

    <div id="alert">
        {{!text}}
    </div>

</body>

</html>