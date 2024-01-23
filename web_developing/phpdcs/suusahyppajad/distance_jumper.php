<?php if (isset($_GET['code'])) {die(highlight_file(__FILE__, 1)); }?>

<?php
require_once ('conf.php');
global $yhendus;

//table for show jumpers which finished jump from bigger to smaller
$kask = $yhendus->prepare("SELECT id, nimi, alustanud, kaugus, valmis FROM suusahyppajad WHERE alustanud=1 AND valmis=1 ORDER BY kaugus DESC");
$kask -> bind_result($id, $nimi, $alustanud, $kaugus, $valmis);
$kask -> execute();
?>



<!DOCTYPE html> 
<html lang="et"> 
 <head>
    <meta charset="UTF-8">
    <title>Hüppajate statiistika</title> 
    <link rel="stylesheet" type="text/css" href="style/style.css">
 </head> 
 <body>
    <?php
    include ('navigation.php');
    ?>

    <h1>Hüppajate statiistika</h1>
    <table>
    <tr>
            <th>ID</th>
            <th>Nimi</th>
            <th>Kaugus</th>
    </tr>
    <?php 
        while($kask->fetch()){
            echo "<tr>";
            echo "<td>".htmlspecialchars($id)."</td>";
            echo "<td>".htmlspecialchars($nimi)."</td>";
            echo "<td>".htmlspecialchars($kaugus)."m"."</td>";
            echo "<tr>";
        }
    ?>
    </table>

</body> 
</html>