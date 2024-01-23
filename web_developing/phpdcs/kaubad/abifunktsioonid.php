<?php
//kuvab andmed 2 tabelist
//sorteerib nimetuse, grupinimi ja hinna järgi
//teeb otsingu tabelis sisestatud teksti järgi
require_once('conf.php');
function kysiKaupadeAndmed($sorttulp="nimetus", $otsisona=""){
    global $yhendus;
    $lubatudtulbad=array("nimetus", "grupinimi", "hind");
    if(!in_array($sorttulp, $lubatudtulbad)){
        return "lubamatu tulp";
    }
    $otsisona=addslashes(stripslashes($otsisona));
    $kask=$yhendus->prepare("SELECT kaubad.id, nimetus, grupinimi, hind  FROM kaubad, kaubagrupid 
 WHERE kaubad.kaubagrupi_id=kaubagrupid.id 
 AND (nimetus LIKE '%$otsisona%' OR grupinimi LIKE '%$otsisona%')  ORDER BY $sorttulp");
    //echo $yhendus->error;
    $kask->bind_result($id, $nimetus, $grupinimi, $hind);
    $kask->execute();
    $hoidla=array();
    while($kask->fetch()){
        $kaup=new stdClass();
        $kaup->id=$id;
        $kaup->nimetus=htmlspecialchars($nimetus);
        $kaup->grupinimi=htmlspecialchars($grupinimi);
        $kaup->hind=$hind;
        array_push($hoidla, $kaup);
    }
    return $hoidla;
}

//делает из названий групп товаров выпадающий список
function looRippMenyy($sqllause, $valikunimi){
    global $yhendus;
    $kask=$yhendus->prepare($sqllause);
    $kask->bind_result($id, $sisu);
    $kask->execute();
    $tulemus="<select name='$valikunimi'>";
    while($kask->fetch()){
        $tulemus.="<option value='$id'>$sisu</option>";
    }
    $tulemus.="</select>";
    return $tulemus;
}
//lisab andmetabeli uus kaubagrupp
function lisaGrupp($grupinimi){
    global $yhendus;

    if (empty($grupinimi)) {
        echo '<script>alert("Sisesta grupp!")</script>';
        return;
    }

    // Kontrolib kas on sama nimi
    $existingGroup = $yhendus->prepare("SELECT grupinimi FROM kaubagrupid WHERE grupinimi = ?");
    $existingGroup->bind_param("s", $grupinimi);
    $existingGroup->execute();
    $existingGroup->store_result();

    // kui nimi on juba olemas, siis alert ja tagasi
    if ($existingGroup->num_rows > 0) {
        echo '<script>alert("Selline grupp on juba olemas!")</script>';
        return;
    }

    // kui nimi ei ole, siis laheb dbsse
    $insertCommand = $yhendus->prepare("INSERT INTO kaubagrupid (grupinimi) VALUES (?)");
    $insertCommand->bind_param("s", $grupinimi);
    $insertCommand->execute();
}


//kustutab tabelist valitud kaup
function kustutaKaup($kauba_id){
    global $yhendus;
    $kask=$yhendus->prepare("DELETE FROM kaubad WHERE id=?");
    $kask->bind_param("i", $kauba_id);
    $kask->execute();
 }
 //kaupa muutmine või uuendamine
function muudaKaup($kauba_id, $nimetus, $kaubagrupi_id, $hind){
    global $yhendus;
    $kask=$yhendus->prepare("UPDATE kaubad SET nimetus=?, kaubagrupi_id=?, hind=?  WHERE kaubad.id=?");
    $kask->bind_param("sidi", $nimetus, $kaubagrupi_id, $hind, $kauba_id);
     $kask->execute();
  
}

function lisa($nimetus, $kaubagrupi_id, $hind) {
    global $yhendus;

    //Kontrollib kas form on saadetud
    if (isset($_REQUEST["kaubalisamine"])) {

        //Kontrollib tuhi read
        if (empty($nimetus) || empty($kaubagrupi_id) || empty($hind)) {
            echo '<script>alert("Sisesta andmed!")</script>';
            return;
        }

        //Kontrollib kas andmed on juba olemas mingites gruppides
        $existingDataCheck = $yhendus->prepare("SELECT COUNT(*) FROM kaubad WHERE nimetus = ?");
        $existingDataCheck->bind_param("s", $nimetus);
        $existingDataCheck->execute();
        $existingDataCheck->bind_result($count);
        $existingDataCheck->fetch();
        $existingDataCheck->close();

        if ($count > 0) {
            echo '<script>alert("Need andmed on juba baasis olemas!")</script>';
            return;
        }

        //Kui andmeid ei ole, siis sissestab
        $insertQuery = $yhendus->prepare("INSERT INTO kaubad (nimetus, kaubagrupi_id, hind) VALUES (?, ?, ?)");
        $insertQuery->bind_param("sdi", $nimetus, $kaubagrupi_id, $hind);
        $insertQuery->execute();
        $insertQuery->close();
    }
}

//1. в файл kaubahaldus.php добавить поиск и сортировку значений в таблице
//2. добавить проверку вводимых значений - нельзя вводить пустой товар и группу товара
//3. при добавлении группы товаров запрещены одинаковые значения /
//4. страница имеет удобный и дружелюбный интерфейс /css
