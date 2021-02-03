<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="bbs/css/style.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>login</title>
</head>

<body>
    <h1>ログイン</h1>
    <form method="post" action="/">
        <div class="clearfix">
            <div id="form">
                <input type="text" id="userId" name="userId" placeholder="ユーザーID">
                <input type="password" id="passWord" name="passWord" placeholder="パスワード">
                <input type="button" onclick="location.href='signUp'" value="新規登録">
                <input type="submit" onclick="location.href='index'" id= "post" value="POST">
            </div>
        </div>
    </form>
    <!-- javascriptの挿入部分 -->
    {{!text}}


</body>

</html>