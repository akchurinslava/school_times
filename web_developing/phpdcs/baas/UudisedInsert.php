<?php

require ('conf.php');
global $yhendus;
//UUdise Lisamine INSERT
if(isset($_REQUEST["teema"])){
    $kask = $yhendus->prepare("INSERT INTO uudised(teema, kuupaev, kirjeldus, varv) VALUES (?,?,?,?)");
    $kask -> bind_param("ssss", $_REQUEST["teema"], $_REQUEST["kuupaev"], $_REQUEST["kirjeldus"], $_REQUEST["varv"]);
    $kask -> execute();
    header("Location: $_REQUEST[PHP_SELF]");
}

?>

<!DOCTYPE html>
<html lang = "et">

<head>
    <meta charset="UTF-8">
    <title>Uudiste leht</title>
</head>
<body>
    <h1>Uudiste leht</h1>
    <h2>Uudise lisamine</h2>
<form name="vorm" action="">
    <input type="text" name="teema">
    <label for="teema">Teema</label>
    <br>

    <input type="date" name="kuupaev" id="kuupaev">
    <label for="kuupaev">Kuupaev</label>
    <br>

    <input type="text" name="kirjeldus" id="kirjeldus">
    <label for="kirjeldus">Kirjeldus</label>
    <br>

    <input type="text" name="varv" id="varv">
    <label for="varv">Varv</label>
    <br>

    <input type="submit" value="OK">

</form>

</body>
</html>