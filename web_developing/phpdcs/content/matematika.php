<!DOCTYPE html>
<html lang="et">
<head>
    <meta charset="UTF-8">
    <title>Vjatseslav php töödeleht</title>
</head>
<body>
<?php
function clearVarsExcept($url, $varname) {
    //return strtok(basename($_SERVER['REQUEST_URI']),"?")."?$varname=".$_REQUEST[$varname];
    return "?$varname=".$_REQUEST[$varname];
}
$number1 = 1;
$number2 = 2;
//vastused - punase värviga ja lisada täpploend
echo "<ol class='mat'><li class='mat1'>Kui me liidame 2 arvu kokku, siis tuleb "."<span>".($number2+$number1)."</span>"."</li>";
echo "<br>";
echo "<li class='mat1'>Kui arv2 jagada arv1-ga, siis tuleb "."<span>".($number2/$number1)."</span>"."</li>";
echo "<br>";
echo "<li class='mat1'>Arv1 ruudus on "."<span>".pow($number1, 2)."</span>"."</li>";
echo "<br>";
echo "<li class='mat1'>arv2-arv1 * 2 = "."<span>";
echo ($number2 - $number1 * 2)."</span>"."</li></ol>";
?>
<h2>Kontrollimiseks sisesta 2 arvu</h2>
<form name="kontroll" action="<?=clearVarsExcept(basename($_SERVER['REQUEST_URI']),"leht")?>" method='post'>
    <input type="number" name="n1">
    <label for="n1">Arv 1</label>
    <br>
    <label for="n2">Arv 2</label>
    <input type="number" name="n2">
    <input type="submit" value="OK">
</form>
<?php
// kontroll
// probleem 1 - leht varvida valgeks, kui arvud on sisetamata
if (isset($_REQUEST["n1"])) {

    if ($_REQUEST["n1"] == $number1) {
        if ($_REQUEST["n2"] == $number2) {
            echo "Õige!";
            echo "<body style='background-color: lightgreen'>";
        } else if ($_REQUEST["n1"] !== $number1) {
            echo "vale!";
            echo "<body style='background-color: lightcoral'>";
        } else {
            echo "<body style='background-color: white'>";
        }
    }
    else {
            echo "vale!";
            echo "<body style='background-color: lightcoral'>";
        }
}