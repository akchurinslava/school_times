<?php
require("abifunktsioonid.php");
$sorttulp = "nimetus";
$otsisona = "";
if (isset($_REQUEST["sort"])) {
    $sorttulp = $_REQUEST["sort"];
}

if (isset($_REQUEST["otsisona"])) {
    $otsisona = $_REQUEST["otsisona"];
}

if(isSet($_REQUEST["grupilisamine"])){
    lisaGrupp($_REQUEST["uuegrupinimi"]);
    header("Location: kaubahaldus.php");
    exit();
}
if(isSet($_REQUEST["kaubalisamine"])){
    lisa($_REQUEST["nimetus"], $_REQUEST["kaubagrupi_id"], $_REQUEST["hind"]);  header("Location: kaubahaldus.php");
    exit();
}
if(isSet($_REQUEST["kustutusid"])){
    kustutaKaup($_REQUEST["kustutusid"]);
}
if(isSet($_REQUEST["muutmine"])){
    muudaKaup($_REQUEST["muudetudid"], $_REQUEST["nimetus"],
        $_REQUEST["kaubagrupi_id"], $_REQUEST["hind"]);  }
$kaubad=kysiKaupadeAndmed($sorttulp, $otsisona);
?>
<a href="highlight.php"> Hightlight</a>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Kaupade leht</title>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <link rel="stylesheet" type="text/css" href="style/style.css">
</head>
<body>
<div id="kauba_width">
<form action="kaubahaldus.php" id="kaubalisamineForm"  onsubmit="return confirmUser('Kas andmed on korras?', 'kaubalisamineForm');">
    
    <h2>Kauba lisamine</h2>
    <dl>
        <dt>Nimetus:</dt>
        <dd><input type="text" name="nimetus"/></dd>
        <dt>Grupp:</dt>
        <dd>
            <?php
            echo looRippMenyy("SELECT id, grupinimi FROM kaubagrupid", "kaubagrupi_id");
            ?>
        </dd>
        <dt>Hind:</dt>
        <dd><input type="text" name="hind" /><input type="submit" name="kaubalisamine" value="Lisa" /></dd>
        
    </dl>
</form>
</div>


<form action="kaubahaldus.php">
<h2>Gruppi lisamine</h2>
    Lisa: <input type="text" name="uuegrupinimi"/>
    <input type="submit" name="grupilisamine" value="Lisa" />
</form>
<form action="?" id="form_table">
    <div id="otsing_width">
    <h2>Kaupade otsing</h2>
   
    Otsi: <input type="text" name="otsisona" />
    <input type="submit" value="Otsi" />
</div>
    <br>
    <br>
    <table>
        <tr>
            <th><a href="kaubahaldus.php?sort=haldus">Haldus</a></th>
            <th><a href="kaubahaldus.php?sort=nimetus">Nimetus</a></th>
            <th><a href="kaubahaldus.php?sort=grupinimi">Grupp</a></th>
            <th><a href="kaubahaldus.php?sort=hind">Hind</a></th>
            
        </tr>
        
            <?php foreach($kaubad as $kaup): ?>
     
        <tr>
            <?php if (isset($_REQUEST["muutmisid"]) && intval($_REQUEST["muutmisid"]) == $kaup->id): ?>
                <td>
                    <form action="kaubahaldus.php">
                       
                        <input type="submit" name="muutmine" value="Muuda" />
                        <input type="submit" name="katkestus" value="Katkesta" />
                        <input type="hidden" name="muudetudid" value="<?= $kaup->id ?>" />
                    </form>
                </td>
                <td><input type="text" name="nimetus" value="<?= $kaup->nimetus ?>" /></td>
                <td><?php echo looRippMenyy("SELECT id, grupinimi FROM kaubagrupid", "kaubagrupi_id"); ?></td>
                <td><input type="text" name="hind" value="<?= $kaup->hind ?>" /></td>
            <?php else: ?>
                <td><a href="kaubahaldus.php?muutmisid=<?= $kaup->id ?>">Muuda</a><a href="kaubahaldus.php?kustutusid=<?= $kaup->id ?>" onclick="return confirm('Kas ikka soovid kustutada?')"> Kustuta</a></td>
                <td><?=$kaup->nimetus ?></td>
                <td><?=$kaup->grupinimi ?></td>
                <td><?=$kaup->hind ?></td>
               
            <?php endif; ?>
        </tr>
    <?php endforeach; ?>
    </table>
</form>
</body>
</html>


<style>
    
    td{
        width: 145px;
        
    }

    table td, th{
        text-align: center;
    }

    #otsing_width{
        margin-left: 180px;
    }

    #kauba_width{
        margin-left: 75px;
    }

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