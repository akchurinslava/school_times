<?php
require("abifunktsioonid.php");
$sorttulp="nimetus";
$otsisona="";
if(isSet($_REQUEST["sort"])){
    $sorttulp=$_REQUEST["sort"];
}
if(isSet($_REQUEST["otsisona"])){
    $otsisona=$_REQUEST["otsisona"];
}
$kaubad=kysiKaupadeAndmed($sorttulp, $otsisona);
?>
<!DOCTYPE html>
<html lang="et">
<head>
    <title>Kaupade leht</title>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />  </head>
<body>
<form action="?">
    Otsi: <input type="text" name="otsisona" />
    <table>
        <tr>
            <th><a href="otsingSort.php?sort=nimetus">Nimetus</a></th>
            <th><a href="otsingSort.php?sort=grupinimi">Kaubagrupp</a></th>
            <th><a href="otsingSort.php?sort=hind">Hind</a></th>
        </tr>
        <?php foreach($kaubad as $kaup): ?>
            <tr>
                <td><?=$kaup->nimetus ?></td>
                <td><?=$kaup->grupinimi ?></td>
                <td><?=$kaup->hind ?></td>
            </tr>
        <?php endforeach; ?>
    </table>
</form>
</body>
</html>