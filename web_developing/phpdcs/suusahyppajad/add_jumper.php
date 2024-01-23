<?php if (isset($_GET['code'])) {die(highlight_file(__FILE__, 1)); }?>

<?php
require_once ('conf.php');
global $yhendus; 

//here we realize jumper add system
if(isset($_REQUEST["nimi"])){
    $kask = $yhendus->prepare("INSERT INTO suusahyppajad(nimi) VALUES (?)");
    $kask -> bind_param("s", $_REQUEST["nimi"]);
    $kask -> execute();
    //$yhendus->close();
    //header("Location: $_REQUEST[PHP_SELF]");
    //header("Location: add_jumper.php");
    //exit;
}
?>


<!DOCTYPE html> 
<html lang="et"> 
 <head>
    <meta charset="UTF-8">
    <title>Hüppaja lisamine</title> 
    <link rel="stylesheet" type="text/css" href="style/style.css">
 </head> 
 <body>
    <?php
    include ('navigation.php');
    ?>
    <h1>Hüppaja lisamine</h1>
    <form name="form" action="">
        <label for="nimi">Nimi:</label>
        <input type="text" name="nimi" id="nimi">
        <input type="submit" value="OK">
    </form>
    <h1>Hüppajate tabel</h1>
    <table>
        <tr>
            <th>ID</th>
            <th>Nimi</th>
            <th>Alustanud</th>
            <th>Kaugus</th>
            <th>Valmis</th>
        </tr>
        <?php
        global $yhendus;
        $kask = $yhendus->prepare("SELECT id, nimi, CASE WHEN alustanud=1 THEN 'Jah' WHEN alustanud=0 THEN 'Ei' ELSE alustanud END AS alustanud, kaugus, CASE WHEN valmis=1 THEN 'Jah' WHEN valmis=0 THEN 'Ei' ELSE valmis END AS valmis FROM suusahyppajad ORDER BY id DESC");
        $kask -> bind_result($id, $nimi, $alustanud, $kaugus, $valmis);
        $kask -> execute();
        while($kask->fetch()){
            echo "<tr>";
            echo "<td>".htmlspecialchars($id)."</td>";
            echo "<td>".htmlspecialchars($nimi)."</td>";
            echo "<td>".htmlspecialchars($alustanud)."</td>";
            echo "<td>".htmlspecialchars($kaugus)."</td>";
            echo "<td>".htmlspecialchars($valmis)."</td>";
            echo "<tr>";
        }
        ?>
    </table>
</body> 
</html>