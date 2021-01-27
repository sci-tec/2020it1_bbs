<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>sign up</title>
</head>

<body>
    <h1>サインアップ</h1>
    <form method="post" action="/signUp">
        <input type="text" id="userName" name="userName" placeholder="ユーザーネーム">
        <input type="text" id="passWord" name="passWord" placeholder="パスワード">
        <input type="submit" onclick="location.href='/'" id="post" value="POST">
    </form>

    <!-- javascript挿入部分 -->
    {{!userId}}
</body>

</html>