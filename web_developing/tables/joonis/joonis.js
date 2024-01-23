function kustuta(){
    let j = document.getElementById("joonis").getContext("2d");
    j.clearRect(0, 0, 400, 300);
}

function ringjoon(){
    let j = document.getElementById("joonis").getContext("2d");
    // ümbermõõt
    j.beginPath();
    j.arc(50, 50, 30, 0, 2*Math.PI, true); //x, y-alguspunkt, 60 - radius
    j.strokeStyle="orange";
    j.stroke();
    //ring
    j.beginPath();
    j.arc(200, 50, 60, 0, 2*Math.PI, true); //x, y-alguspunkt, 60 - radius
    j.fillStyle="orange";
    j.fill();
}

function joon(){
    let j = document.getElementById("joonis").getContext("2d");
    j.beginPath();
    j.moveTo(200, 150); //alguspunkt
    j.lineTo(300, 180);
    j.lineTo(300, 250);
    j.lineTo(200, 150); //lõppunk
    j.strokeStyle="orange";
    j.lineWidth="2";
    j.stroke();
    
}


function ristkylik(){
    let j = document.getElementById("joonis").getContext("2d");
    let laius = parseInt(document.getElementById("laius").value);
    let korgus = parseInt(document.getElementById("korgus").value);
    j.fillStyle="red";
    j.fillRect(100, 100, laius, korgus);  //x, y, laius, kõrgus

}

function koos(){
    ristkylik();
    ringjoon();
    joon();
}