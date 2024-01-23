<?php
function clearVarsExcept($url, $varname) {
    //return strtok(basename($_SERVER['REQUEST_URI']),"?")."?$varname=".$_REQUEST[$varname];
    return "?$varname=".$_REQUEST[$varname];
}
$tekst='Tore et on teisipaev';

echo $tekst;
echo "<br>";

echo strtolower($tekst);
echo "<br>";

echo strtoupper($tekst);
echo "<br>";

echo ucwords($tekst);
echo "<br>";

echo strlen($tekst);
echo "<br>";

echo str_word_count($tekst);
echo "<br>";

//eraldab lauses alates 4 kokku 5 tahte
echo substr($tekst, 3, 5);
echo '<br>';
//Esimesed 4 tahte
echo substr($tekst, 0, 4);
echo '<br>';
echo substr($tekst, -8, 7);
echo '<br>';
// tuhiku asukoht tekstis
$otsitav = 'on';
echo strpos($tekst, "on");
echo '<br>';

echo "esimese tuhiku asukoht tekstis".strpos($tekst, " ");
echo '<br>';

echo substr($tekst, strpos($tekst, " "), strlen($tekst)-strpos($tekst, " "));
//moistatus
//Eesti linn
//5 tints
//control - insert town and page show right or not
?>

<hr>
<h2>Moistatus. Eesti linn</h2>
<?php
$linn = 'maardu';
echo "<ol><li>Linnanimi pikkus on ".strlen($linn)." tahte</li>";
echo "<br>";
echo "<li>Linnanimi esimesed 2 tahed ".substr($linn, 0, 2)."</li>";
echo "<br>";
echo "<li>Linnanimi viimased 2 tahed ".substr($linn, 4, 6)."</li>";
echo "<br>";
echo "<li>Palju sõnade linna nimi -  ".str_word_count($linn)." sõna</li>";
echo "<br>";
echo "<li>Millises positsionil asub taht R - ".strpos($linn, "r")." positsionil</li></ol>";
?>
<h2>Vastus</h2>
<form name="kontroll" action="<?=clearVarsExcept(basename($_SERVER['REQUEST_URI']),"leht")?>" method='post'>
    <input type="text" name="linn">
    <label for="linn">text</label>
    <input type="submit" value="OK">
    <br>
<?php

if (isset($_REQUEST["linn"])) {
    if ($_REQUEST["linn"] == $linn) {
        echo "RIGHT!";
        echo "<body style='background: green'>";
    }
    else{
        echo "FALSE!";
        echo "<body style='background: red'>";
    }
}
echo '<br>';
highlight_file('tekstifunktsioonid.php');
