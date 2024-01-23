function legs(){
    let canv = document.getElementById("canv").getContext("2d");
    canv.beginPath();
    canv.moveTo(120, 476);
    canv.lineTo(120, 359);
    canv.lineTo(216, 359);
    canv.lineTo(216, 476);
    canv.lineTo(199, 476);
    canv.lineTo(199, 385);
    canv.lineTo(137, 385);
    canv.lineTo(137, 476);
    canv.lineTo(120, 476);
    canv.strokeStyle="red";
    canv.lineWidth="2";
    canv.fillStyle="red";
    canv.fill();
    canv.stroke();
}

function body_k(){
    let canv = document.getElementById("canv").getContext("2d");
    canv.beginPath();
    canv.moveTo(120, 359);
    canv.lineTo(120, 254);
    canv.lineTo(216, 254);
    canv.lineTo(216, 359);
    canv.lineTo(120, 359);
    canv.strokeStyle="black";
    canv.lineWidth="2";
    canv.fillStyle="black";
    canv.fill();
    canv.stroke();

}

function neck(){
    let canv = document.getElementById("canv").getContext("2d");
    canv.beginPath();
    canv.moveTo(141, 254);
    canv.lineTo(141, 246);
    canv.lineTo(196, 246);
    canv.lineTo(196, 254);
    canv.strokeStyle="yellow";
    canv.lineWidth="2";
    canv.fillStyle="yellow";
    canv.fill();
    canv.stroke();
}

function head_k(){
    let canv = document.getElementById("canv").getContext("2d");
    canv.beginPath();
    canv.arc(168, 214, 43, 0, 2*Math.PI, true);
    canv.fillStyle="yellow";
    canv.fill();
}

function face_k(){
    let canv = document.getElementById("canv").getContext("2d");
    canv.beginPath();
    canv.moveTo(156, 230);
    canv.lineTo(183, 230);
    canv.lineTo(183, 241);
    canv.lineTo(156, 241);
    canv.lineTo(156, 230);
    canv.moveTo(159, 230);
    canv.lineTo(159, 241);
    canv.moveTo(163, 230);
    canv.lineTo(163, 241);
    canv.moveTo(170, 230);
    canv.lineTo(170, 241);
    canv.moveTo(175, 230);
    canv.lineTo(175, 241);
    canv.moveTo(180, 230);
    canv.lineTo(180, 241);
    //
    canv.moveTo(149, 207);
    canv.lineTo(188, 207);
    canv.lineTo(208,200);
    //
    canv.moveTo(149, 207);
    canv.lineTo(129,200);

    //
    canv.strokeStyle="black";
    canv.lineWidth="2";
    canv.stroke();
    canv.beginPath();
    canv.arc(150, 213, 5, 0, 2*Math.PI, true);
    canv.strokeStyle="black";
    canv.stroke();
    canv.fillStyle="white";
    canv.fill();
    //
    canv.beginPath();
    canv.arc(150, 213, 1, 0, 2*Math.PI, true);
    canv.strokeStyle="black";
    canv.stroke();
    canv.fillStyle="black";
    canv.fill();
    //
    canv.beginPath();
    canv.arc(188, 213, 5, 0, 2*Math.PI, true);
    canv.strokeStyle="black";
    canv.stroke();
    canv.fillStyle="white";
    canv.fill();
    //
    canv.beginPath();
    canv.arc(188, 213, 1, 0, 2*Math.PI, true);
    canv.strokeStyle="black";
    canv.stroke();
    canv.fillStyle="black";
    canv.fill();
}

function fire(){
    let canv = document.getElementById("canv").getContext("2d");
    canv.beginPath();
    canv.moveTo(239, 250);
    canv.lineTo(239, 258);
    canv.moveTo(237, 250);
    canv.lineTo(237, 258);
    canv.moveTo(235, 250);
    canv.lineTo(235, 258);
    canv.strokeStyle="orange";
    canv.lineWidth="2";
    canv.stroke();

}

function ciga(){
    let canv = document.getElementById("canv").getContext("2d");
    canv.beginPath();
    canv.moveTo(180, 241);
    canv.lineTo(239, 250);
    canv.lineTo(239, 258);
    canv.lineTo(170, 241);
    canv.lineTo(180, 241);
    canv.strokeStyle="white";
    canv.lineWidth="2";
    canv.fillStyle="white";
    canv.fill();
    canv.stroke();
    fire();
}


function arms(){
    let canv = document.getElementById("canv").getContext("2d");
    canv.beginPath();
    canv.moveTo(215, 268);
    canv.lineTo(256, 320);
    canv.lineTo(215, 400);
    canv.lineTo(215, 390);
    canv.lineTo(235, 320);
    canv.lineTo(215, 300);
    canv.lineTo(215, 268);
    canv.fillStyle="yellow";
    canv.fill();
    canv.strokeStyle="yellow";
    canv.lineWidth="2";
    canv.stroke();

    //second arms
    canv.moveTo(120, 268);
    canv.lineTo(79, 320);
    canv.lineTo(120, 400);
    canv.lineTo(120, 390);
    canv.lineTo(100, 320);
    canv.lineTo(120, 300);
    canv.lineTo(120, 268);
    canv.strokeStyle="yellow";
    canv.lineWidth="2";
    canv.stroke();
    canv.fillStyle="yellow";
    canv.fill();
}


function bottle(){
    let canv = document.getElementById("canv").getContext("2d");
    canv.beginPath();
    canv.moveTo(240, 476);
    canv.lineTo(240, 430);
    canv.lineTo(250 , 420);
    canv.lineTo(250 , 400);
    canv.lineTo(257 , 400);
    canv.lineTo(257, 420);
    canv.lineTo(267, 430);
    canv.lineTo(267, 476);
    canv.lineTo(240, 476);
    canv.strokeStyle="brown";
    canv.lineWidth="2";
    canv.fillStyle="brown";
    canv.fill();
    canv.stroke();
}


function delete_k(){
    let j = document.getElementById("canv").getContext("2d");
    j.clearRect(0, 0, 400, 480);
}

function together(){
    arms();
    head_k();
    face_k();
    neck();
    legs();
    body_k();
    ciga();
    bottle();
}


