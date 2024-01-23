<!DOCTYPE HTML>
<html lang="et">
<head>
    <meta charset="UTF-8">
    <title>Githubtask</title>
    <link rel="stylesheet" type="text/css" href="style/style.css">
</head>
<body>
<?php
for ($index = 1; $index <= 19; $index += 2){
    echo $index. ' ';
}

echo "<br>";
echo "<br>";
for ($index1 = 1; $index1 <= 9; $index1++){
    for ($index2 = 0; $index2 <= 9; $index2++){
        echo $index1.','. $index2 .' ';
    }
}
echo "<br>";
echo "<br>";
$naitleja = array();
$naitleja_count = 0;

for ($i = 1; $i <= 10; $i++){
    $naitleja[] = "Naitleja".$i;
    echo $naitleja[$naitleja_count]."<br>";
    $naitleja_count+=1;
}
echo "<br>";
echo "<br>";

$person = array(
    'nimi' => 'Dima',
    'vanus' => '18',
    'kodakondsus' => 'Eesti',
    'elukoht' => 'Tallinn',
    'keel' => 'vene'
    );
echo "Tema nimi on ".$person['nimi']." ja ta on ".$person['vanus']." aastat vana,"." ta on ".$person['kodakondsus']." kodanik".". Ta elab ".$person['elukoht']." ja ta raagib ".$person['keel']." keelt.";
echo "<br>";
echo "<br>";

$loomad = array();
$loomade_nimid = array(
    "karu",
    "tiger",
    "lovi",
    "jaanes",
    "kass",
    "huny",
    "koer",
    "varblane",
    "elevant",
    "ziraf"
);
foreach ($loomade_nimid as $loom) {
    $loomad[] = $loom;
}
foreach ($loomad as $loom){
    echo $loom."<br>";
}

echo "<br>";
echo "<br>";

$filmid = array(
    array("Alibaba", "Jaanes", "Torn"),
    array("Hunt ja Ani", "Galaktik", "Spider-man"),
    array("Opetaja", "Maa", "Eesti")
);
for ($index = 0; $index < 3; $index++) {
    for ($index2 = 0; $index2 < 3; $index2++) {
        echo $filmid[$index][$index2];
        if ($index2 < 2) {
            echo ", ";
        }else{
            echo ".";
        }
    }
    echo "<br>";
}
?>

</body>
</html>
