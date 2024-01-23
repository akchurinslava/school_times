<?php

$servernimi = "localhost";
$kasutajanimi = "slava";
$parool = "12345";
$andmebaas = "slava";
$yhendus = new mysqli($servernimi, $kasutajanimi, $parool, $andmebaas);
$yhendus->set_charset('UTF8');
//yhenduse kontroll
if(!$yhendus){
    die('Ei saa ühendust andmebaasiga');
}

?>