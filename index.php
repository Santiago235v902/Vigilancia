<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="post">
        <h1>Bienvenido</h1>
        <input type="text" name="name" placeholder="Colocar su noombre">
        <input type="password" name="contraseña" id="*" placeholder="Colocar su contraseña">
        <input type="text" name="dni" placeholder="Colocar su dni">
        <input type="submit" name="register">
    </form>
    <?php
    include("registrar.php");
    ?>
</body>
</html>