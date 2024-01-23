<?php
require ('conf.php');
global $yhendus;
//Kala Lisamine INSERT
if(isset($_REQUEST["lisamisvorm"])){
    $kask = $yhendus->prepare("INSERT INTO kalad(kalanimi, pilt, varv) VALUES (?,?,?)");
    $kask -> bind_param("sss", $_REQUEST["kalanimi"], $_REQUEST["pilt"], $_REQUEST["varv"]);
    $kask -> execute();
    header("Location: $_SERVER[PHP_SELF]");
}

if(isset($_REQUEST["kustuta"])){
    $kask = $yhendus->prepare("DELETE FROM kalad WHERE id=?");
    $kask->bind_param("i", $_REQUEST["kustuta"]);
    $kask->execute();
}
?>

<!DOCTYPE html>
<html lang = "et">

<head>
    <meta charset="UTF-8">
    <title>Kalade leht</title>
    <link rel="stylesheet" type="text/css" href="style/style.css">
</head>
<body>
    <h1>Kalade andmebaas</h1>
    <div id="lingid">
    <?php
        global $yhendus;
        $kask = $yhendus->prepare("SELECT id, kalanimi, varv FROM kalad");
        $kask -> bind_result($id, $kalanimi, $varv);
        $kask -> execute();
        echo "<ul>";

        while ($kask->fetch()){
            echo "<li><a href='?id=$id'>".$kalanimi." ".$varv."</a></li>";
            }
            echo "</ul>";
        echo "<a href='?lisa=jah'>Lisa...</a>";
        
    ?>
    </div>

    <div id="sisu">
        <?php
            if(isset($_REQUEST["id"])){
                $kask = $yhendus->prepare("SELECT id, kalanimi, pilt, varv FROM kalad WHERE id=?");
                $kask->bind_param("i", $_REQUEST["id"]);
                $kask->bind_result($id, $kalanimi, $pilt, $varv);
                $kask->execute();
                if($kask->fetch()){
                
                    echo "<div style='background-color: $varv; width:300px;'>";
                    echo "<strong>".$id.", ".$kalanimi.", ".$varv;
                    echo "<img src='$pilt' alt='$kalanimi'><td><a href='?kustuta=$id'>Delete</a></td>";
                    echo "</div>";
                }
            }
        ?>
    </div>
    <?php
    if(isset($_REQUEST["lisa"])){
    ?>
    <h2>Kala lisamine</h2>
    <form name="vorm" action="?">
    <input type="hidden" name="lisamisvorm" value="jah">
    <input type="text" name="kalanimi">
    <label for="kalanimi">Kalanimi</label>
    <br>

    <input type="text" name="pilt" id="kirjeldus">
    <label for="pilt">Pilt</label>
    <br>

    <input type="text" name="varv" id="varv">
    <label for="varv">Varv</label>
    <br>

    <input type="submit" value="OK">

    </form>
    <?php
    }
    ?>



<?php
$yhendus->close();
?>
</body>
</html>