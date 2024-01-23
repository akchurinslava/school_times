<?php  
 require_once("conf.php"); 
 session_start(); 
 if(!empty($_REQUEST["korras_id"])){ 
 $kask=$yhendus->prepare( 
 "UPDATE jalgrattaeksam SET ringtee=1 WHERE id=?"); 
$kask->bind_param("i", $_REQUEST["korras_id"]); 
$kask->execute(); 
 } 
 if(!empty($_REQUEST["vigane_id"])){ 
 $kask=$yhendus->prepare( 
 "UPDATE jalgrattaeksam SET ringtee=2 WHERE id=?"); 
$kask->bind_param("i", $_REQUEST["vigane_id"]); 
$kask->execute(); 
 } 
 $kask=$yhendus->prepare("SELECT id, eesnimi, perekonnanimi   FROM jalgrattaeksam WHERE teooriatulemus>=9 AND slaalom = 1 AND ringtee = -1");  $kask->bind_result($id, $eesnimi, $perekonnanimi); 
 $kask->execute(); 
?> 
<!doctype html> 
<html lang="et"> 
 <head>
 <link rel="stylesheet" type="text/css" href="style/style.css"> 
 <title>Ringtee</title> 
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
     <h1>Ringtee</h1> 

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