function kustuta(){
    let j=document.getElementById("joonis").getContext("2d")
    j.clearRect(0, 0, 520, 566)
}

function joonista(){
    jalad();
    jeans();
    keha();
    muster();
    shoulders();
    hands();
    kael();
    ears();
    pea();
    face();
}

function jalad(){
    let j = document.getElementById("joonis").getContext("2d");

    j.fillStyle = "#d0b070";
    j.strokeStyle = "#807040";
    j.lineWidth = 2;

    j.strokeRect(135, 520, 110, 25);//Ð»ÐµÐ²Ð°Ñ Ð½Ð¾Ð³Ð°
    j.fillRect(135, 520, 110, 25);

    j.strokeRect(265, 520, 110, 25);//Ð¿Ñ€Ð°Ð²Ð°Ñ Ð½Ð¾Ð³Ð°
    j.fillRect(265, 520, 110, 25);

    j.strokeRect(135, 430, 240, 25); //Ð¿Ð¾ÑÑ
    j.fillRect(135, 430, 240, 25);
}

function jeans(){
    let j = document.getElementById("joonis").getContext("2d");

    j.fillStyle = "#e0d090";
    j.strokeStyle = "#807040";
    j.lineWidth = 2;

    j.moveTo(135,520);
    j.lineTo(135,455);
    j.lineTo(375, 455);
    j.lineTo(375,520);
    j.lineTo(265,520);
    j.lineTo(265,465);
    j.lineTo(245,465);
    j.lineTo(245, 520);
    j.lineTo(135, 520);
    j.closePath();

    j.stroke();
    j.fillRect(135, 455, 110,65)
    j.fillRect(265, 455, 110, 65)
    j.fillRect(245, 455, 20, 10)
}

function keha() {
    let k = document.getElementById("joonis").getContext("2d");

    k.strokeStyle = "#807040";
    k.fillStyle = "#e0d090";

    k.beginPath();
    k.moveTo(105, 430);
    k.lineTo(405, 430);
    k.lineTo(355, 210);
    k.lineTo(155, 210);
    k.lineTo(105, 430);
    k.closePath();

    k.stroke(); // Ð Ð¸ÑÐ¾Ð²Ð°Ð½Ð¸Ðµ ÐºÐ¾Ð½Ñ‚ÑƒÑ€Ð°
    k.fill(); // Ð—Ð°ÐºÑ€Ð°ÑÐºÐ° Ñ„Ð¸Ð³ÑƒÑ€Ñ‹
}

function muster(){
    let m = document.getElementById("joonis").getContext("2d");

    m.beginPath();
    m.moveTo(190, 212);
    m.lineTo(220, 315);
    m.lineTo(235, 430);
    m.lineTo(275, 430);
    m.lineTo(290, 315);
    m.lineTo(320, 212);
    m.lineTo(255, 247);
    m.lineTo(190, 212);
    m.closePath();
    m.lineWidth = 3;
    m.strokeStyle = "#303010";
    m.stroke();
    m.fillStyle = "#a08040";
    m.fill();

    m.beginPath();
    m.moveTo(220, 315);
    m.lineTo(290, 315); // Ð³Ð¾Ñ€Ð¸Ð·Ð¾Ð½Ñ‚Ð°Ð»ÑŒÐ½Ð°Ñ Ð¿Ñ€ÑÐ¼Ð°Ñ Ð»Ð¸Ð½Ð¸Ñ Ð¿Ð¾ÑÐµÑ€ÐµÐ´Ð¸Ð½Ñ‹ ÐºÐ¾Ñ„Ñ‚Ñ‹
    m.stroke();

    m.beginPath();
    m.moveTo(227, 370);
    m.lineTo(286, 350);
    m.stroke();

    m.beginPath();
    m.moveTo(233,415);
    m.lineTo(277, 415); // Ð³Ð¾Ñ€Ð¸Ð·Ð¾Ð½Ñ‚Ð°Ð»ÑŒÐ½Ð°Ñ Ð¿Ñ€ÑÐ¼Ð°Ñ Ð»Ð¸Ð½Ð¸Ñ Ð²Ð½Ð¸Ð·Ñƒ ÐºÐ¾Ñ„Ñ‚Ñ‹
    m.stroke();

    m.beginPath();
    m.moveTo(260, 415);
    m.lineTo(260,430); //Ð²ÐµÑ€Ñ‚Ð¸ÐºÐ°Ð»ÑŒÐ½Ð°Ñ Ð¿Ñ€ÑÐ¼Ð°Ñ Ð»Ð¸Ð½Ð¸Ñ Ð² ÑÐ°Ð¼Ð¾Ð¼ Ð½Ð¸Ð·Ñƒ ÐºÐ¾Ñ„Ñ‚Ñ‹
    m.stroke();

    m.beginPath();
    m.moveTo(255,245);
    m.lineTo(255,315);
    m.stroke();

    m.beginPath();
    m.moveTo(196,230);
    m.lineTo(240,256);
    m.stroke();

    m.beginPath();
    m.moveTo(314,230);
    m.lineTo(265,256);
    m.stroke();
}

function shoulders(){
    let s = document.getElementById("joonis").getContext("2d");

    s.beginPath();
    s.moveTo(110, 225);
    s.lineTo(65, 315);
    s.lineTo(55, 405);
    s.lineTo(100, 415);
    s.lineTo(110, 405)
    s.lineTo(105,340);
    s.lineTo(135, 290);
    s.lineTo(151,225);
    s.lineTo(110, 225);
    s.closePath();
    s.strokeStyle = "#807040";
    s.stroke();
    s.fillStyle = "#e0d090";
    s.fill();

    s.beginPath();
    s.moveTo(359, 225);
    s.lineTo(400, 225);
    s.lineTo(455, 315);
    s.lineTo(455, 405);
    s.lineTo(410, 415);
    s.lineTo(400, 405);
    s.lineTo(405,340);
    s.lineTo(375,290);
    s.lineTo(359,225);
    s.strokeStyle = "#807040";
    s.stroke();
    s.fillStyle = "#e0d090";
    s.fill();
}

function hands() {
    let h = document.getElementById("joonis").getContext("2d");

    let startingAngle = 1.25 * Math.PI;
    let endingAngle = 2.25 * Math.PI;

    h.beginPath();
    h.arc(50, 450, 25,  startingAngle, endingAngle, false); // Ð Ð¸ÑÑƒÐµÐ¼ Ð´ÑƒÐ³Ñƒ
    h.lineWidth = 20; // Ð¨Ð¸Ñ€Ð¸Ð½Ð° Ð»Ð¸Ð½Ð¸Ð¸
    h.strokeStyle = "#707030"; // Ð¦Ð²ÐµÑ‚ Ð»Ð¸Ð½Ð¸Ð¸
    h.lineCap = "round";
    h.stroke(); // Ð Ð¸ÑÑƒÐµÐ¼ Ð»Ð¸Ð½Ð¸ÑŽ, Ð»ÐµÐ²Ð°Ñ Ñ€ÑƒÐºÐ°

    h.beginPath();
    h.moveTo(50, 430);
    h.lineTo(65, 400);
    h.lineTo(75, 395);
    h.lineTo(90, 400);
    h.lineTo(95, 410);
    h.lineTo(80, 440);
    h.lineTo(55, 430);
    h.closePath();
    h.lineWidth = 2;
    h.stroke();
    h.fillStyle = "#707030";
    h.fill();

    let firstAngle = 0.75 * Math.PI;
    let lastAngle = 1.75 * Math.PI;

    h.beginPath();
    h.arc(450, 450, 25, firstAngle, lastAngle, false); // Ð Ð¸ÑÑƒÐµÐ¼ Ð´ÑƒÐ³Ñƒ
    h.lineWidth = 20; // Ð¨Ð¸Ñ€Ð¸Ð½Ð° Ð»Ð¸Ð½Ð¸Ð¸
    h.strokeStyle = "#707030"; // Ð¦Ð²ÐµÑ‚ Ð»Ð¸Ð½Ð¸Ð¸
    h.lineCap = "round";
    h.stroke(); // Ð Ð¸ÑÑƒÐµÐ¼ Ð»Ð¸Ð½Ð¸ÑŽ, Ð¿Ñ€Ð°Ð²Ð°Ñ Ñ€ÑƒÐºÐ°

    h.beginPath();
    h.moveTo(420, 435);
    h.lineTo(410, 405);
    h.lineTo(415, 395);
    h.lineTo(435, 390);
    h.lineTo(445, 395);
    h.lineTo(445, 435);
    h.lineTo(420, 435);
    h.closePath();
    h.lineWidth = 2;
    h.stroke();
    h.fillStyle = "#707030";
    h.fill();
}

function kael() {
    let a = document.getElementById("joonis").getContext("2d");

    a.fillStyle = "#707030";
    a.strokeStyle = "#707030";

    a.strokeRect(190, 185, 130, 25);
    a.fillRect(190, 185, 130, 25); //ÑˆÐµÑ

    a.beginPath();
    a.moveTo(190, 210);
    a.lineTo(255, 245);
    a.lineTo(320, 210);
    a.lineTo(190, 210);
    a.closePath();

    a.stroke(); // Ð Ð¸ÑÐ¾Ð²Ð°Ð½Ð¸Ðµ ÐºÐ¾Ð½Ñ‚ÑƒÑ€Ð°
    a.fill();
}

function ears(){
    let e = document.getElementById("joonis").getContext("2d");

    e.beginPath();
    e.moveTo(55, 75);
    e.lineTo(70, 65);
    e.lineTo(90, 65);
    e.lineTo(120, 70);
    e.lineTo(160, 65);
    e.lineTo(180, 70);
    e.lineTo(160, 130);
    e.lineTo(145,135);
    e.lineTo(80,85);
    e.lineTo(55,75);
    e.closePath();
    e.strokeStyle = "#707030";
    e.stroke();
    e.fillStyle = "#707030";
    e.fill();

    e.beginPath();
    e.moveTo(70, 75);
    e.lineTo(90, 75);
    e.lineTo(120, 85);
    e.lineTo(160, 80);
    e.lineTo(175, 85);
    e.lineTo(163, 120);
    e.lineTo(145, 125);
    e.lineTo(85,80);
    e.lineTo(70, 75);
    e.closePath();
    e.strokeStyle = "#303010";
    e.stroke();
    e.fillStyle = "#303010";
    e.fill();

    e.beginPath();
    e.moveTo(330, 70);
    e.lineTo(350, 65);
    e.lineTo(390, 70);
    e.lineTo(420, 65);
    e.lineTo(440, 65);
    e.lineTo(455, 75);
    e.lineTo(430, 85);
    e.lineTo(365, 135);
    e.lineTo(350, 130);
    e.lineTo(330, 70);
    e.closePath();
    e.strokeStyle = "#707030";
    e.stroke();
    e.fillStyle = "#707030";
    e.fill();

    e.beginPath();
    e.moveTo(440, 75);
    e.lineTo(420, 75);
    e.lineTo(390, 85);
    e.lineTo(350, 80);
    e.lineTo(335, 85);
    e.lineTo(347, 120);
    e.lineTo(365, 125);
    e.lineTo(425, 80);
    e.lineTo(440, 75);
    e.closePath();
    e.strokeStyle = "#303010";
    e.stroke();
    e.fillStyle = "#303010";
    e.fill();
}

function pea() {
    let b = document.getElementById("joonis").getContext("2d");

    b.beginPath();
    b.arc(255, 110, 100, 0, 2 * Math.PI, true);
    b.fillStyle = "#707030";
    b.fill();

    b.beginPath();
    b.arc(237, 40, 35, 0, Math.PI, true);
    b.closePath();
    b.fillStyle = "#707030";
    b.fill();

    b.beginPath();
    b.arc(273, 40, 35, 0, Math.PI, true);
    b.closePath();
    b.fillStyle = "#707030";
    b.fill();

    b.beginPath();
    b.arc(205, 55, 35, 15, 5);
    b.closePath();
    b.fillStyle = "#707030";
    b.fill();

    b.beginPath();
    b.arc(305, 50, 35, 0, 2 * Math.PI);
    b.closePath();
    b.fillStyle = "#707030";
    b.fill();
    b.strokeStyle = "#707030";
    b.stroke();

    let sAngle = 1.5 * Math.PI;
    let eAngle = 2 * Math.PI;
    let stAngle = 1.4 * Math.PI;
    let enAngle = Math.PI;

    b.beginPath();
    b.arc(210, 42, 20,  sAngle, eAngle, false); // Ð Ð¸ÑÑƒÐµÐ¼ Ð´ÑƒÐ³Ñƒ
    b.lineWidth = 5; // Ð¨Ð¸Ñ€Ð¸Ð½Ð° Ð»Ð¸Ð½Ð¸Ð¸
    b.strokeStyle = "#303010"; // Ð¦Ð²ÐµÑ‚ Ð»Ð¸Ð½Ð¸Ð¸
    b.lineCap = "round";
    b.stroke(); //Ð»ÐµÐ²Ð°Ñ ÑÐºÐ»Ð°Ð´ÐºÐ° Ð½Ð° Ð³Ð¾Ð»Ð¾Ð²Ðµ

    b.beginPath();
    b.arc(305, 42, 25,  stAngle, enAngle, true); // Ð Ð¸ÑÑƒÐµÐ¼ Ð´ÑƒÐ³Ñƒ
    b.lineWidth = 5; // Ð¨Ð¸Ñ€Ð¸Ð½Ð° Ð»Ð¸Ð½Ð¸Ð¸
    b.strokeStyle = "#303010"; // Ð¦Ð²ÐµÑ‚ Ð»Ð¸Ð½Ð¸Ð¸
    b.lineCap = "round";
    b.stroke(); //Ð¿Ñ€Ð°Ð²Ð°Ñ ÑÐºÐ»Ð°Ð´ÐºÐ° Ð½Ð° Ð³Ð¾Ð»Ð¾Ð²Ðµ

    b.beginPath();
    b.moveTo(255, 13);
    b.lineTo(255, 40);
    b.strokeStyle = "#303010";
    b.lineWidth = 5;
    b.stroke(); //Ð¿Ñ€ÑÐ¼Ð°Ñ ÑÐºÐ»Ð°Ð´ÐºÐ° Ð¿Ð¾ÑÐµÑ€ÐµÐ´Ð¸Ð½Ðµ
}

function face(){
    let f = document.getElementById("joonis").getContext("2d");

    f.beginPath();
    f.arc(255, 105, 15, Math.PI * 0.1, Math.PI*0.9, false);
    f.lineWidth = 5;
    f.lineCap = "round";
    f.strokeStyle = "#303010";
    f.stroke(); //Ð½Ð¾Ñ

    f.beginPath();
    f.arc(255, 115, 15, Math.PI * 1.15, Math.PI * 1.9, false);
    f.lineWidth = 5;
    f.lineCap = "round";
    f.strokeStyle = "#303010";
    f.stroke(); //Ð½Ð¾Ñ

    f.beginPath();
    f.arc(255, 105, 15, Math.PI * 1.15, Math.PI * 1.85, false);
    f.lineWidth = 2;
    f.lineCap = "round";
    f.strokeStyle = "#303010";
    f.stroke(); //ÑÐºÐ»Ð°Ð´ÐºÐ° Ð½Ð°Ð´ Ð½Ð¾ÑÐ¾Ð¼

    f.beginPath();
    f.arc(205, 105, 25, Math.PI * 0.1, Math.PI * 0.95, false); // ÑƒÐ²ÐµÐ»Ð¸Ñ‡ÐµÐ½Ñ‹ ÑƒÐ³Ð»Ñ‹
    f.lineWidth = 5;
    f.lineCap = "round";
    f.fillStyle = "#FFFFFF"; // Ñ†Ð²ÐµÑ‚ Ð·Ð°Ð¿Ð¾Ð»Ð½ÐµÐ½Ð¸Ñ
    f.fill(); // Ð·Ð°ÐºÑ€Ð°ÑˆÐ¸Ð²Ð°Ð½Ð¸Ðµ Ð²Ð½ÑƒÑ‚Ñ€ÐµÐ½Ð½ÐµÐ¹ Ñ‡Ð°ÑÑ‚Ð¸
    f.strokeStyle = "#303010";
    f.stroke(); // Ð»ÐµÐ²Ñ‹Ð¹ Ð³Ð»Ð°Ð·

    f.beginPath();
    f.arc(205, 115, 25, Math.PI * 1.05, Math.PI * 1.95, false); // ÑƒÐ²ÐµÐ»Ð¸Ñ‡ÐµÐ½Ñ‹ ÑƒÐ³Ð»Ñ‹
    f.lineWidth = 5;
    f.lineCap = "round";
    f.fillStyle = "#FFFFFF"; // Ñ†Ð²ÐµÑ‚ Ð·Ð°Ð¿Ð¾Ð»Ð½ÐµÐ½Ð¸Ñ
    f.fill(); // Ð·Ð°ÐºÑ€Ð°ÑˆÐ¸Ð²Ð°Ð½Ð¸Ðµ Ð²Ð½ÑƒÑ‚Ñ€ÐµÐ½Ð½ÐµÐ¹ Ñ‡Ð°ÑÑ‚Ð¸
    f.strokeStyle = "#303010";
    f.stroke(); // Ð»ÐµÐ²Ñ‹Ð¹ Ð³Ð»Ð°Ð·


    f.beginPath();
    f.arc(305, 105, 25, Math.PI * 0.1, Math.PI * 0.95, false);
    f.lineWidth = 5;
    f.lineCap = "round";
    f.fillStyle = "#FFFFFF"; // Ñ†Ð²ÐµÑ‚ Ð·Ð°Ð¿Ð¾Ð»Ð½ÐµÐ½Ð¸Ñ
    f.fill(); // Ð·Ð°ÐºÑ€Ð°ÑˆÐ¸Ð²Ð°Ð½Ð¸Ðµ Ð²Ð½ÑƒÑ‚Ñ€ÐµÐ½Ð½ÐµÐ¹ Ñ‡Ð°ÑÑ‚Ð¸
    f.strokeStyle = "#303010";
    f.stroke(); //Ð¿Ñ€Ð°Ð²Ñ‹Ð¹ Ð³Ð»Ð°Ð·

    f.beginPath();
    f.arc(305, 115, 25, Math.PI * 1.05, Math.PI * 1.95, false);
    f.lineWidth = 5;
    f.lineCap = "round";
    f.fillStyle = "#FFFFFF"; // Ñ†Ð²ÐµÑ‚ Ð·Ð°Ð¿Ð¾Ð»Ð½ÐµÐ½Ð¸Ñ
    f.fill(); // Ð·Ð°ÐºÑ€Ð°ÑˆÐ¸Ð²Ð°Ð½Ð¸Ðµ Ð²Ð½ÑƒÑ‚Ñ€ÐµÐ½Ð½ÐµÐ¹ Ñ‡Ð°ÑÑ‚Ð¸
    f.strokeStyle = "#303010";
    f.stroke(); //Ð¿Ñ€Ð°Ð²Ñ‹Ð¹ Ð³Ð»Ð°Ð·

    f.beginPath();
    f.moveTo(205, 110);
    f.lineTo(224, 112);
    f.strokeStyle = "#FFFFFF";
    f.stroke();

    f.beginPath();
    f.moveTo(305, 110);
    f.lineTo(324, 112);
    f.strokeStyle = "#FFFFFF";
    f.stroke();

    f.beginPath();
    f.arc(205, 110, 17, Math.PI*2, 0, true);
    f.closePath();
    f.fillStyle = "#000000"
    f.fill(); //Ð»ÐµÐ²Ñ‹Ð¹ Ð·Ñ€Ð°Ñ‡Ð¾Ðº

    f.beginPath();
    f.arc(305, 110, 17, Math.PI*2, 0, true);
    f.closePath();
    f.fillStyle = "#000000"
    f.fill(); //Ð¿Ñ€Ð°Ð²Ñ‹Ð¹ Ð·Ñ€Ð°Ñ‡Ð¾Ðº

    f.beginPath();
    f.arc(202, 105, 5, Math.PI*2, 0, true);
    f.closePath();
    f.fillStyle = "#FFFFFF"
    f.fill(); //Ð»ÐµÐ²Ñ‹Ð¹ Ð·Ñ€Ð°Ñ‡Ð¾Ðº

    f.beginPath();
    f.arc(302, 105, 5, Math.PI*2, 0, true);
    f.closePath();
    f.fillStyle = "#FFFFFF"
    f.fill(); //Ð¿Ñ€Ð°Ð²Ñ‹Ð¹ Ð·Ñ€Ð°Ñ‡Ð¾Ðº

    f.beginPath();
    f.arc(205, 95, 25, Math.PI * 1.15, Math.PI * 1.85, false);
    f.lineWidth = 2;
    f.lineCap = "round";
    f.strokeStyle = "#303010";
    f.stroke(); //ÑÐºÐ»Ð°Ð´ÐºÐ° Ð½Ð°Ð´ Ð»ÐµÐ²Ñ‹Ð¼ Ð³Ð»Ð°Ð·Ð¾Ð¼

    f.beginPath();
    f.arc(305, 95, 25, Math.PI * 1.15, Math.PI * 1.85, false);
    f.lineWidth = 2;
    f.lineCap = "round";
    f.strokeStyle = "#303010";
    f.stroke(); //ÑÐºÐ»Ð°Ð´ÐºÐ° Ð½Ð°Ð´ Ð¿Ñ€Ð°Ð²Ñ‹Ð¼ Ð³Ð»Ð°Ð·Ð¾Ð¼

    let stAngle = 1.35 * Math.PI;
    let enAngle = Math.PI * 0.8;

    f.beginPath();
    f.arc(245, 155, 25,  stAngle, enAngle, true); // Ð Ð¸ÑÑƒÐµÐ¼ Ð´ÑƒÐ³Ñƒ
    f.lineWidth = 2; // Ð¨Ð¸Ñ€Ð¸Ð½Ð° Ð»Ð¸Ð½Ð¸Ð¸
    f.strokeStyle = "#303010"; // Ð¦Ð²ÐµÑ‚ Ð»Ð¸Ð½Ð¸Ð¸
    f.lineCap = "round";
    f.stroke(); //Ð»ÐµÐ²Ð°Ñ ÑÐºÐ»Ð°Ð´ÐºÐ° Ð¿Ð¾Ð´ Ð½Ð¾ÑÐ¾Ð¼

    let strAngle = 1.65 * Math.PI;
    let endAngle = 0.2 * Math.PI;

    f.beginPath();
    f.arc(265, 155, 25,  strAngle, endAngle, false); // Ð Ð¸ÑÑƒÐµÐ¼ Ð´ÑƒÐ³Ñƒ
    f.lineWidth = 2; // Ð¨Ð¸Ñ€Ð¸Ð½Ð° Ð»Ð¸Ð½Ð¸Ð¸
    f.strokeStyle = "#303010"; // Ð¦Ð²ÐµÑ‚ Ð»Ð¸Ð½Ð¸Ð¸
    f.lineCap = "round";
    f.stroke(); //Ð¿Ñ€Ð°Ð²Ð°Ñ ÑÐºÐ»Ð°Ð´ÐºÐ° Ð½Ð° Ð³Ð¾Ð»Ð¾Ð²Ðµ

    f.beginPath();
    f.arc(255, 130, 25, Math.PI * 0.3, Math.PI * 0.7, false); // Ð¸Ð·Ð¼ÐµÐ½ÐµÐ½Ñ‹ ÑƒÐ³Ð»Ñ‹ Ð¸ Ð½Ð°Ð¿Ñ€Ð°Ð²Ð»ÐµÐ½Ð¸Ðµ
    f.lineWidth = 5;
    f.lineCap = "round";
    f.strokeStyle = "#303010";
    f.stroke(); //Ð³ÑƒÐ±Ñ‹

    f.beginPath();
    f.arc(255, 150, 15, Math.PI * 0.3, Math.PI * 0.7, false); // Ð¸Ð·Ð¼ÐµÐ½ÐµÐ½Ñ‹ ÑƒÐ³Ð»Ñ‹ Ð¸ Ð½Ð°Ð¿Ñ€Ð°Ð²Ð»ÐµÐ½Ð¸Ðµ
    f.lineWidth = 2;
    f.lineCap = "round";
    f.strokeStyle = "#303010";
    f.stroke(); // ÑÐºÐ»Ð°Ð´ÐºÐ° Ð¿Ð¾Ð´ Ð³ÑƒÐ±Ð¾Ð¹

    f.beginPath();
    f.arc(255, 160, 50, Math.PI * 0.3, Math.PI * 0.7, false); // Ð¸Ð·Ð¼ÐµÐ½ÐµÐ½Ñ‹ ÑƒÐ³Ð»Ñ‹ Ð¸ Ð½Ð°Ð¿Ñ€Ð°Ð²Ð»ÐµÐ½Ð¸Ðµ
    f.lineWidth = 2;
    f.lineCap = "round";
    f.strokeStyle = "#303010";
    f.stroke(); // Ñ€Ð°Ð·Ð³Ñ€Ð°Ð½Ð¸Ñ‡Ð¸Ñ‚ÐµÐ»ÑŒ Ð³Ð¾Ð»Ð¾Ð²Ñ‹ Ð¸ ÑˆÐµÐ¸ = Ð¿Ð¾Ð´Ð±Ð¾Ñ€Ð¾Ð´Ð¾Ðº
}