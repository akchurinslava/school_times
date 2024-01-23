<head>
    <meta charset="UTF-8">
    <title>Ylesanded</title>
    <link rel="stylesheet" type="text/css" href="style/style.css">
</head>
<body>
    <h1>Ylesanne 1</h1>
<?php
//ulesanne 1, vjatseslav, 26.08.1994
$nimi = "Dima";
$sunniaasta = "29.10.1990";
$tahtkuu = "Oven";
$abc = "'\'";

echo "Tema nimi on ".$nimi."<br>";
echo "Tema sunniaasta on ".$sunniaasta."<br>";
echo "Tema tahtkuu on ".$tahtkuu."<br>";
echo "\"It's My Life\" - Dr. Alban"."<br>";
echo "(".substr($abc, 1, 1)."(".substr($abc, 1, 1)."<br>";
echo "( -.- )"."<br>";
echo 'o_(")(")';
?>
    <h1>Ylesanne 2</h1>

<?php
//ulesanne 2, vjatseslav, 26.08.1994
$a = 4.5;
$b = 5.5;
echo "esimene arv on ".$a." ja teine on ".$b;
echo "<br>";
echo $a += $b;
echo "<br>";
echo $a -= $b;
echo "<br>";
echo $a *= $b;
echo "<br>";
echo $a /= $b;
echo "<br>";
echo $a %= $b;
echo "<br>";
echo "<br>";
$mm = 1000;
$cm = 10;
$m = 1;
$arv = 3204;
echo "arv on ".$arv."<br>";
$arv1 = $arv / $mm;
$arv2 = $arv / $cm;
$arv3 = $arv / $m;
$arv1_v = sprintf('arv m on: %0.2f', $arv1);
$arv2_v = sprintf('arv cm on: %0.2f', $arv2);
$arv3_v = sprintf('arv mm on: %0.2f', $arv3);
echo $arv1_v."<br>";
echo $arv2_v."<br>";
echo $arv3_v."<br>";
echo "<br>";
echo "<br>";
$ac = 2.8;
$cb = 2.1;
$ab = 3.5;
$P = $ac + $cb + $ab;
$h = $ac * $cb / $ab;
$S = $ab * $h / 2;
echo "AC pikkus on ".$ac."<br>";
echo "CB pikkus on ".$cb."<br>";
echo "AB pikkus on ".$ab."<br>";
echo "Umbermõõt on ".$P."<br>";
echo "Pindala on ".$S; 
?>
    <h1>Ylesanne 3</h1>
<?php
//ulesanne 3, vjatseslav, 26.08.1994
$nimi = "aLeXi";
$nimi = strtolower($nimi);
echo "Tere ".ucfirst($nimi)."<br>";
$sona = "stalker";
$sona = strtoupper($sona);
echo $sona[0].".".$sona[1].".".$sona[2].".".$sona[3].".".$sona[4].".".$sona[5].".".$sona[6]."."."<br>";
$tekst = "Sa oled täielik noob";
$replace = "***";
$tekst_change = str_word_count($tekst, 1);
echo str_replace($tekst_change[4], $replace, $tekst)."<br>";
$mail = "Ülle ja Doos";
$mail = str_replace("Ü", "y", $mail);
$mail = strtolower($mail);
$mail_masiiv = str_word_count($mail, 1);
echo $mail_masiiv[0].".";
echo $mail_masiiv[2]."@hkhk.edu.ee";

?>

</body>