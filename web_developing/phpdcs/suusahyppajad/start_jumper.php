<?php if (isset($_GET['code'])) {die(highlight_file(__FILE__, 1)); }?>

<?php
require_once ('conf.php');
global $yhendus;

//here we realize distance editing
if(!empty($_REQUEST["kaugus"])){
    $kask2=$yhendus->prepare( 
    "UPDATE suusahyppajad SET kaugus=?, valmis=1 WHERE id=?"); 
    $kask2->bind_param("ii", $_REQUEST["kaugus"], $_REQUEST["id"]);
    $kask2->execute();

    //header("Location: $_REQUEST[PHP_SELF]");
    //header("Location: start_jumper.php");
}

//here we accept jumpers for start possition, so we set alustanud to 1 from 0
if(!empty($_REQUEST["start_id"])){
    $kask=$yhendus->prepare(
    "UPDATE suusahyppajad SET alustanud=1 WHERE id=?"); 
    $kask->bind_param("i", $_REQUEST["start_id"]);
    $kask->execute();
    //header("Location: $_REQUEST[PHP_SELF]");
    //header("Location: start_jumper.php");
} 

//first table for distance editing
$kask2 = $yhendus->prepare("SELECT id, nimi, alustanud, kaugus, valmis FROM suusahyppajad WHERE alustanud=1 AND kaugus=0 ORDER BY kaugus DESC LIMIT 1");
$kask2->execute();
$kask2->store_result(); //store result of query, if not we catch an error about double query to SQL
$kask2->bind_result($id, $nimi, $alustanud, $kaugus, $valmis);

//here we realize only jumpers who already started, but not finished jump
$kask = $yhendus->prepare("SELECT id, nimi, alustanud, kaugus, valmis FROM suusahyppajad WHERE alustanud=0 ORDER BY alustanud DESC");
$kask->execute();
$kask->store_result(); //store result of query, if not we catch an error about double query to SQL
$kask->bind_result($id, $nimi, $alustanud, $kaugus, $valmis);
?>

<!DOCTYPE html>
<html lang="et"> 
 <head>
    <meta charset="UTF-8">
    <title>Hüppe alustamine ja kauguse sisenemine</title> 
    <link rel="stylesheet" type="text/css" href="style/style.css">
 </head> 
 <body>
    <?php
    include ('navigation.php');
    ?>
    <h1>Hüppe alustamine</h1>
        <table>
        <?php
        while($kask->fetch()){
            echo "<tr>";
            echo "<td>".htmlspecialchars($nimi)."</td>";
            echo "<td>";
            echo"Accept: <a href='?start_id=$id'>Yes</a>";
            echo"</td>";
            echo "<tr>";
        }
        ?>
        </table>
    <h1>Kauguse sisenemine</h1>
        <table> 
        <?php 
        while($kask2->fetch()){ 
            echo" 
                <tr> 
                <td>$nimi</td> 
                <td><form action=''> 
                <input type='hidden' name='id' value='$id'/> 
                <input type='number' name='kaugus'/>
                <input type='submit' value='Sisesta kauguse'/> 
                </form> 
                </td> 
                </tr> 
                "; 
        } 
        ?> 
        </table>

</body> 
</html>