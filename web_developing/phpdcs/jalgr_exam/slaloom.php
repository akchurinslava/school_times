<?php  
 require_once("conf.php");
 session_start();  
 if(!empty($_REQUEST["korras_id"])){
    //uuendab tabeliandmed --> slaalom = 1
 global $yhendus; 
 $kask=$yhendus->prepare(
 "UPDATE jalgrattaeksam SET slaalom=1 WHERE id=?"); 
$kask->bind_param("i", $_REQUEST["korras_id"]);
$kask->execute();
 } 
 if(!empty($_REQUEST["vigane_id"])){
    //uuendab tabeliandmed --> slaalom = 2 kui vajutakse ebaonnestunud
 $kask=$yhendus->prepare(
 "UPDATE jalgrattaeksam SET slaalom=2 WHERE id=?"); 
$kask->bind_param("i", $_REQUEST["vigane_id"]); 
$kask->execute(); 
 }
 //veebileht kuvab ainult need kellel teooriatulemus => 10 and slaalom =- 1 
 $kask=$yhendus->prepare("SELECT id, eesnimi, perekonnanimi   FROM jalgrattaeksam WHERE teooriatulemus>=10 AND slaalom=-1 OR slaalom = 2");  $kask->bind_result($id, $eesnimi, $perekonnanimi); 
 $kask->execute(); 
?> 
<!doctype html> 
<html lang="et"> 
 <head>
 <link rel="stylesheet" type="text/css" href="style/style.css">  
 <title>Slaalom</title> 
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
    <h1>Slaalom</h1> 
 <table> 
 <?php 
 while($kask->fetch()){ 
 echo " 
 <tr> 
 <td>$eesnimi</td> 
 <td>$perekonnanimi</td> 
 <td> 
 <a href='?korras_id=$id'>Korras</a>
 <a href='?vigane_id=$id'>Ebaõnnestunud</a> 
 </td> 
</tr> 
 "; 
} 
 ?> 
</table> 

<?php } ?>
 </body> 
</html> 