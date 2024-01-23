<?php
require_once("conf.php");  
session_start();

 if(!empty($_REQUEST["teooriatulemus"])){
    if(preg_match('/[a-zA-Z]/', $_REQUEST["teooriatulemus"])){
        echo "Cant contain words!";
    }
    else{
    //naita ainult need opilased kellel tulemus on sisemata
        $kask=$yhendus->prepare( 
        "UPDATE jalgrattaeksam SET teooriatulemus=? WHERE id=?"); 
        $kask->bind_param("ii", $_REQUEST["teooriatulemus"], $_REQUEST["id"]);
        $kask->execute();
    }
}
 $kask=$yhendus->prepare("SELECT id, eesnimi, perekonnanimi   FROM jalgrattaeksam WHERE teooriatulemus=-1 OR teooriatulemus=2"); 
 $kask->bind_result($id, $eesnimi, $perekonnanimi); 
 $kask->execute();
?> 
<!doctype html> 
<html lang="et">
 <head>
 <link rel="stylesheet" type="text/css" href="style/style.css"> 
 <title>Teooriaeksam</title> 
 </head> 
 <body>
   <header>
    <?php
    if(isset($_SESSION['kasutaja'])){
        ?>
        <a>Tere, <?="$_SESSION[kasutaja]"?></a>
        <a href="logout.php">Logi välja</a>
        <?php
    } else {
        ?>
        <a href="login.php">Logi sisse</a>
        <?php
    }
    ?>
</header>
<?php
include ('navig.php');
?>

   <?php
    if (isset($_SESSION['kasutaja'])){

    ?>
    <h1>Teooriaeksami tulemuste sissetamine</h1>
 <table> 
 <?php

 while($kask->fetch()){ 
 echo " 
 <tr> 
 <td>$eesnimi</td> 
 <td>$perekonnanimi</td> 
 <td><form action=''> 
 <input type='hidden' name='id' value='$id' />";

 if(isset($_SESSION["kasutaja"])){
 echo "
 <input type='text' name='teooriatulemus' />
 <input type='submit' value='Sisesta tulemus' />
 </form> 
 </td> 
</tr>
 "; 
};
 }
 ?> 
</table> 
<?php
}
?>
 </body> 
</html>