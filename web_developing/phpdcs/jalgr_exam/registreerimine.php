<?php  
 require_once("conf.php");
 session_start(); 
 if(isSet($_REQUEST["sisestusnupp"])){
    if(preg_match('#[0-9]#', $_REQUEST["perekonnanimi"]) || preg_match('#[0-9]#', $_REQUEST["eesnimi"]) || empty($_REQUEST["perekonnanimi"]) || empty($_REQUEST["eesnimi"])){
        echo "!";
    }else{
        $kask=$yhendus->prepare(
        "INSERT INTO jalgrattaeksam(eesnimi, perekonnanimi) VALUES (?, ?)"); $kask->bind_param("ss", $_REQUEST["eesnimi"], $_REQUEST["perekonnanimi"]); $kask->execute(); 
        $yhendus->close();
        header("Location: $_SERVER[PHP_SELF]?lisatudeesnimi=$_REQUEST[eesnimi]");
        header("Location: teooria.php");
        exit(); 
 }
}
?> 
<!doctype html> 
<html lang="et"> 
 <head>  
 <title>Kasutaja registreerimine</title>
 <link rel="stylesheet" type="text/css" href="style/style.css">
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
 <h1>Registreerimine</h1> 
 <!-- if tahame, et 25,26 tootavad, siis on vaja kustuta 10 -->
 <!-- <?php 
 if(isSet($_REQUEST["lisatudeesnimi"])){ 
 echo "Lisati $_REQUEST[lisatudeesnimi]"; 
 } 
 ?>  -->
<form action="?"> 
 <dl> 
 <dt>Eesnimi:</dt> 
<dd><input type="text" name="eesnimi" /></dd> 
 <dt>Perekonnanimi:</dt> 
<dd><input type="text" name="perekonnanimi" /></dd> 
 <dt><input type="submit" name="sisestusnupp" value="sisesta" /></dt>  </dl> 
</form> 
 </body> 
</html> 

<style>
    dl {
        display: grid;
        grid-template-columns: 1fr 2fr;
        grid-gap: 10px;
        margin-bottom: 15px;
    }

    dt {
        font-weight: bold;
    }

    dd {
        margin: 0;
    }
</style>