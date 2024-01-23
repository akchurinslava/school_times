<?php
require ('conf.php');
global $yhendus;
//uuendamine, punktide lisamine
if(isset($_REQUEST["healaul"])){
    $kask = $yhendus -> prepare("UPDATE eestilaul SET punktid=punktid+1 where id=?");
    $kask->bind_param("i", $_REQUEST["healaul"]);
    $kask->execute();
    header("Location: $_SERVER[PHP_SELF]");
}
//kommentaaride lisamine
if(isset($_REQUEST["uuskomment"])){
    if(!empty($_REQUEST["komment"])){
        $kask = $yhendus -> prepare("UPDATE eestilaul SET kommentaarid=CONCAT(IFNULL(kommentaarid, ''), ?) where id=?");
        $lisakomment = $_REQUEST["komment"]."\n";
        $kask->bind_param("si", $lisakomment, $_REQUEST["uuskomment"]);
        $kask->execute();
        header("Location: $_SERVER[PHP_SELF]");
        //lisa responsive zebra table css - DONE
        //kustutamine - komment koik voi viimane punkt
        //update - minus punkt
    }

}

if(isset($_REQUEST["kustuta"])){
    $kask = $yhendus->prepare("UPDATE eestilaul SET kommentaarid=REPLACE(kommentaarid, SUBSTRING_INDEX(kommentaarid, '\n', -2), '') where id=?");
    $kask->bind_param("s", $_REQUEST["kustuta"]);
    $kask->execute();
    header("Location: $_SERVER[PHP_SELF]");
}

if(isset($_REQUEST["pahalaul"])){
    $kask = $yhendus -> prepare("UPDATE eestilaul SET punktid=punktid-1 where id=?");
    $kask->bind_param("i", $_REQUEST["pahalaul"]);
    $kask->execute();
    header("Location: $_SERVER[PHP_SELF]");
}


?>

<!DOCTYPE html>
<html lang = "et">

<head>
    <meta charset="UTF-8">
    <title>Eesti laulukonkurss</title>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body>
    <h1>Eesti laulukonkurss</h1>
    <table class="w3-table-all w3-hoverable w3-centered">
    <tr>
        <thead> 
        <th>Lalunimi</th>
        <th>Laulja</th>
        <th>Punktid</th>
        <th></th>
        <th>Kommentaarid</th>
        </thead>
    </tr>
    <?php
    //andmete kuvamine andmebaasist tabelist
    global $yhendus;
    $kask = $yhendus->prepare("SELECT id, laulunimi, laulja, punktid, kommentaarid FROM eestilaul");
    $kask -> bind_result($id, $laulunimi, $laulja, $punktid, $kommentaarid);
    $kask -> execute();
    

    while ($kask->fetch()){
        echo "<tr>";
        echo "<td>".$laulunimi."</td>";
        echo "<td>".$laulja."</td>";
        echo "<td>".$punktid."</td>";
        echo "<td><a href='?healaul=$id'>Lisa 1punkt</a><br><a href='?pahalaul=$id'>Minus 1punkt</a></td>";
        echo "<td>".nl2br(htmlspecialchars($kommentaarid))."<a href='?kustuta=$id'>Delete</a></td>";
        echo "<td>
<form action='?'>
<input type='hidden' value='$id' name='uuskomment'>
<input type='text' name='komment'>
<input type='submit' value='OK'>
</form>
        
</td>";
        echo "</tr>";
    }

    ?>
</table>


<?php
$yhendus->close();
?>
</body>
</html>