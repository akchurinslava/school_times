<?php if (isset($_GET['code'])) { die(highlight_file(__FILE__, 1)); } ?>
<?php
require ('conf.php');
global $yhendus;
//add osalejad
if(isset($_REQUEST["nimi"])){
    $kask = $yhendus->prepare("INSERT INTO osalejad(nimi, telefon, pilt, sunniaeg) VALUES (?,?,?,?)");
    $kask -> bind_param("ssss", $_REQUEST["nimi"], $_REQUEST["telefon"], $_REQUEST["pilt"], $_REQUEST["sunniaeg"]);
    $kask -> execute();
    //header("Location: $_SERVER[PHP_SELF]");
}
?>

<!DOCTYPE html>
<html lang = "et">
<head>
    <meta charset="UTF-8">
    <title>Matkaleht</title>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <style>
        #subm{
            position: relative;
            margin-left: 8px;
        }
    </style>
</head>
<body>


<table class="w3-table-all w3-hoverable">
<tr>
  <th>Nimi</th>
  <th>Telefon</th>
  <th>Sunniaeg</th>
  <th>Vanus</th>
  <th></th>
</tr>
<tr>
  <td>dasd</td>
  <td>dasd</td>
  <td>ddasd</td>
  <td>Vanus</td>
  <td>jah</td>
</tr>
</table>
<br>
<br>
<form name="vorm" form class="w3-container" action="matka.php">
<div class="w3-row-padding">
  <div class="w3-half">
    <label for="nimi">Nimi:</label>
    
    <input class="w3-input w3-border" type="text" placeholder="Nimi" name="nimi" id="nimi">
  </div>
  <div class="w3-half">
  <label for="telefon">Telefon:</label>
    <input class="w3-input w3-border" type="text" placeholder="Telefon" name="telefon" id="telefon">
  </div>
  <div class="w3-half">
  <label for="pilt">Pilt:</label>
    <input class="w3-input w3-border" type="text" placeholder="Pilt" name="pilt" id="pilt">
  </div>
  <div class="w3-half">
    <label for="sunniaeg">Sunniaeg:</label>
    <input class="w3-input w3-border" type="text" placeholder="Sunniaeg" name="sunniaeg" id="sunniaeg"> 
  </div>
  <button class="w3-button w3-green" type="submit" id="subm">Submit</button>
</div>
</form>
<br>
<br>

<?php
$yhendus->close();
?>

</body>
</html>