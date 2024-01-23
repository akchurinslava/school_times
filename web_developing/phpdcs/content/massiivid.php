<!DOCTYPE HTML>
<html lang="et">
<head>
    <meta charset="UTF-8">
    <title>Masiivid</title>
    <link rel="stylesheet" type="text/css" href="style/style.css">
</head>
<body>
<h2>Tudrukud</h2>
<?php
$tudrukud = array('mari', 'kati', 'rebeka', 'katlin', 'grete', 'diana', 'ani', 'inga');
sort($tudrukud);
foreach($tudrukud as $tudruk){
    echo $tudruk."<br>"; 
}
?>

<h2>Tudrukud 2</h2>
<?php
for ($index = 0; $index < 3; $index++){
    echo $tudrukud[$index]."<br>";
}
echo "<br>";
echo end($tudrukud);
echo "<br>";
echo "<br>";
$len = count($tudrukud);
$random_name = rand(0, $len-1);
echo $tudrukud[$random_name];
?>
<h2>Autod</h2>
<?php
$autod = array("Subaru","BMW","Acura","Mercedes-Benz","Lexus","GMC","Volvo","Toyota","Volkswagen","Volkswagen","GMC","Jeep","Saab","Hyundai","Subaru","Mercedes-Benz",
"Honda","Kia","Mercedes-Benz","Chevrolet","Chevrolet","Porsche","Buick","Dodge","GMC","Dodge","Nissan","Dodge","Jaguar","Ford","Honda","Toyota","Jeep",
"Kia","Buick","Chevrolet","Subaru","Chevrolet","Chevrolet","Pontiac","Maybach","Chevrolet","Plymouth","Dodge","Nissan","Porsche","Nissan","Mercedes-Benz",
"Suzuki","Nissan","Ford","Acura","Volkswagen","Lincoln","Mazda","BMW","Mercury","Mitsubishi","Ram","Audi","Kia","Pontiac","Toyota","Acura","Toyota","Toyota",
"Chevrolet","Oldsmobile","Acura","Pontiac","Lexus","Chevrolet","Cadillac","GMC","Jeep","Audi","Acura","Acura","Honda","Dodge","Hummer","Chevrolet","BMW",
"Honda","Lincoln","Hummer","Acura","Buick","BMW","Chevrolet","Cadillac","BMW","Pontiac","Audi","Hummer","Suzuki","Mitsubishi","Jeep","Buick","Ford");
$vin = array("1GKS1GKC8FR966658", "1FTEW1C87AK375821", "1G4GF5E30DF760067", "1FTEW1CW9AF114701", "WAUGGAFC8CN433989", "3G5DA03E83S704506", "4JGDA2EB0DA207570", 
"1FTEW1E88AK070552", "SAJWA0F77F8732763", "JHMFA3F21BS660717", "JTHBP5C29C5750730", "WA1LFAFP9DA963060", "3D7TT2CT6BG521976", "WVWN7EE961049", 
"2C3CA5CG3BH341234", "YV4952CFXC162587", "KNALN4D71F5805172", "JN1CV6EK7BM903692", "5FRYD3H84EB186765", "WAUL64B83N441878", "WDDGF4HBXCF845665", 
"WAUKF78E45A133973", "JN1BY0AR2AM022612", "WA1EY74L69D931520", "3GYFNGEYXBS290465", "1D7CW2GK4AS059336", "JN8AZ1FY5EW087447", "WAUBF78E57A343355", 
"SCFFBCCD8AG695133", "WBAWC73548E143482", "3GYFNGE38DS093883", "SCBCP73WC348460", "JN8AE2KPXE9353316", "2C3CDXDT2EH018229", "1G6AH5SX7D0325662", 
"WVWED7AJ7DW431402", "1FTKR1AD3AP316066", "WBAKF5C52CE612586", "1FTNX2A57AE16083", "WAUCFAFR1AA166821", "SCFFDAAM3EG486065", "1G4PR5SK5F4821043", 
"1C3CDFCB4ED858321", "1N6AD0CW8EN722090", "1NXBU4EE0AZ438077", "2T1BPRHE7FC131594", "JH4KB1637C451183", "1C4NJCBA7ED747024", "WAUHF68P86A736691", 
"3D7TT2HT1AG96429", "5GADX23L96D250838", "5FRYD3H25FB985936", "1G4GG5E30DF126304", "KNADH5A38B6072755", "WAUBFAFL1BA477979", "3C63DRL4CG674293", 
"1G6AR5SX0E0834815", "1NXBU4EE2AZ309838", "WAUKGBFB4AN797783", "JN1AJ0HP8AM801887", "WAUPL68E25A448831", "WA1C8BFP3FA535374", "WAUHE78P78A019744", 
"TRURD38J081400551", "1G4HP52K95428171", "5N1CR2MN1EC607241", "5UMDU93417L322773", "1G6AJ5S35F09585", "JN1CV6AP3BM234743", "SCBCR63W66C842051", 
"SCFFDCBD2AG509467", "WBA3C1C58CA664091", "1D7RW2BK6BS922303", "WAUDH98E67A546009", "2HNYB1H46CH683844", "3VW467AT4DM257275", "WDDGF4HB7CA515172", 
"2G61W5S88E9666199", "5GADV33W17D256205", "2C3CDXDT9CH683075", "2G4GU5X0E9989574", "WAUJC58E53A641651", "WDDEJ7KB3CA053774", "3D73M3CL6AG890452", 
"5GAER13D19J026924", "1G4HC5EM1BU329204", "3VWML7AJ6CM772736", "3C6TD4HT2CG011211", "JTDZN3EU2FJ023675", "JN8AZ1MU4CW041721", "KNAFX5A82F5991024", 
"1N6AA0CJ1D57470", "WAUEG98E76A780908", "WAUAF78E96A920706", "1GT01XEG8FZ268942", "1FTEW1CW4AF371278", "JN1AZ4EH8DM531691", "WAUEKAFBXAN294295", 
"1N6AA0EDXFN868772", "WBADW3C59DJ422810");
echo count($autod);
echo "<br>";
echo "<br>";
if(count($autod) == count($vin)){
    echo "equal";
}else{
    echo "not equal";
};
echo "<br>";
echo "<br>";
$toyota = "Toyota";
$audi = "Audi";
$toyota_count = 0;
$audi_count = 0;
foreach($autod as $auto){
    if($auto === $toyota){
        $toyota_count++;
    }else if($auto === $audi){
        $audi_count++;
    }
}
echo "Toyota arv: ".$toyota_count,"<br>";
echo "Audi arv: ".$audi_count,"<br>";
echo "<br>";
foreach($vin as $vinkood){
    if(strlen($vinkood) < 17){
        echo $vinkood."<br>";
    }
}
?>

<h2>Palgad</h2>
<?php
$palgad = array(1220,1213,1295,1312,1298,1354,1296,1286,1292,1327,1369,1455);
echo "Keskimne 2018 aasta palk on ".array_sum($palgad) / count($palgad);
?>
<h2>Firmad</h2>
<?php
$firmad = array("Kimia","Mynte","Voomm","Twiyo","Layo","Talane","Gigashots","Tagchat","Quaxo","Voonyx","Kwilith","Edgepulse","Eidel","Eadel","Jaloo","Oyope","Jamia");
sort($firmad);
foreach($firmad as $firma){
    echo $firma."; ";
}

?>
<br>
<br>
<form method="post">
<input type="text" placeholder="sisesta firma nimi" name="firma_name">
<input type="submit" value="OK">
</form>
<?php
$deleted = false;
if ($_SERVER["REQUEST_METHOD"] === "POST"){
    $firma_delete = $_POST["firma_name"];
    $key = array_search($firma_delete, $firmad);
    if ($key !== false) {
        unset($firmad[$key]);
        $deleted = true;
        if ($deleted === true){
            foreach($firmad as $firma){
                echo $firma."; ";
            }
        }
    }
}
?>
<h2>Riigid</h2>
<?php
$riigid = array("Indonesia","Canada","Kyrgyzstan","Germany","Philippines",
"Philippines","Canada","Philippines","South Sudan","Brazil",
"Democratic Republic of the Congo","Indonesia","Syria","Sweden",
"Philippines","Russia","China","Japan","Brazil","Sweden","Mexico","France",
"Kazakhstan","Cuba","Portugal","Czech Republic");
$riik_name = "";
foreach ($riigid as $riik){
    if (strlen($riik) > strlen($riik_name)){
        $riik_name = $riik;
    }
}
echo $riik_name;
?>
<h2>Hinna nimed</h2>
<?php
$hinna_nimid = array("瀚聪","月松","雨萌","展博","雪丽","哲恒","慧妍","博裕","宸瑜","奕漳",
"思宏","伟菘","彦歆","睿杰","尹智","琪煜","惠茜","晓晴","志宸","博豪",
"璟雯","崇杉","俊誉","军卿","辰华","娅楠","志宸","欣妍","明美");

sort($hinna_nimid);
foreach ($hinna_nimid as $nimi){
    echo $nimi."<br>";
}
echo "<br>";
echo "Eesimene nimi: ".$hinna_nimid[0];
echo "<br>";
echo "Viimane nimi: ".end($hinna_nimid);
?>
<h2>Hinna nimed</h2>
<form method="post">
<input type="text" placeholder="sisesta nimi" name="nimi">
<input type="submit" value="OK">
</form>
<?php
$google = array("Feake","Bradwell","Dreger","Bloggett","Lambole","Daish","Lippiett","
Blackie","Stollenbeck","Houseago","Dugall","Sprowson","Kitley","Mcenamin",
"Allchin","Doghartie","Brierly","Pirrone","Fairnie","Seal","Scoffins",
"Galer","Matevosian","DeBlase","Cubbin","Izzett","Ebi","Clohisey",
"Prater","Probart","Samwaye","Concannon","MacLure","Eliet","Kundt","Reyes");

if ($_SERVER["REQUEST_METHOD"] === "POST"){
    if (in_array($_POST["nimi"], $google)){
        echo "Nimi ".$_POST["nimi"]." on massiivis";
    }else{
        echo "Nimi ".$_POST["nimi"]." ei ole massiivis";
    }
}
?>
<h2>Pildid</h2>
<?php
$pildid = array("prentice.jpg","freeland.jpg","peterus.jpg","devlin.jpg","gabriel.jpg","pete.jpg");
$pildid_path = '/Applications/XAMPP/xamppfiles/htdocs/phpdcs/pildid/';
if (isset($pildid[2])){
    $image_source = $pildid_path.$pildid[2];
    echo '<img src="'.$image_source .'" alt="Kolmas pilt">';
}else{
    echo 'Kolmandaid pilte pole';
}
echo "<br>";
echo "<br>";
foreach ($pildid as $pilt){
    $image_source = $imagePath.$pilt;
    echo '<img src="'.$image_source .'" alt="' .$pilt .'">';
}
?>
</body>
</html>