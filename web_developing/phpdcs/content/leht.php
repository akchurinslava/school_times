<!DOCTYPE HTML>
<html lang="et">
<head>
    <meta charset="UTF-8">
    <title>Küsimustik</title>
    <link rel="stylesheet" type="text/css" href="style/style.css">
    <script src="js/form_script2.js"></script>
</head>
<body>   
        <h1>TARKVARAARENDAJA KÜSIMUSTIK</h1>
        <form name="Küsimustik">
        <div class="back">
        <div class="global_container">
        <div class="row">
        <div class="column1">
            <div id="name">
                <strong><label for="name1">Sisesta oma nimi:</label></strong>
                <input type="text" name="name1" id="name1" placeholder="Eesnimi" oninput="name_abs()">
            </div>
        </div>
        <div class="column2">
            <div id="answer_name"></div>
        </div>
        </div>
        <div class="row">
        <div class="column1">
            <div class="container">
                <input id="age" type="range" min="0" max="100" step="1" oninput="range_form()">
                <span id="spanvanus">Vanus: <output id="value"></output></span>
                <script>
                    const value = document.querySelector("#value")
                    const input = document.querySelector("#age")
                    value.textContent = input.value
                    input.addEventListener("input", (event) => {
                        value.textContent = event.target.value
                    })
                </script>
            </div>
            </div>
            <div class="column2">
                <div id="answer_age"></div>
            </div>
            </div>
            <div class="row">
            <div class="column1">
            <div id="level">
                <strong>Vali oma kogemuse tarkvaraarendamises:</strong>
                <br>
                <input type="radio" name="exp" id="1-2years" value="1-2 aastat" onchange="level()">
                <label for="1-2years">1-2 aastat</label>
                <input type="radio" name="exp" id="2-5years" value="2-5 aastat" onchange="level()">
                <label for="2-5years">2-5 aastat</label>
                <input type="radio" name="exp" id="5-10years" value="5-10 aastat" onchange="level()">
                <label for="5-10years">5-10 aastat</label>
                <br>
                <input type="radio" name="exp" id="10+years" value="10+ aastat" onchange="level()">
                <label for="10+years">10+ aastat</label>
            </div>
            </div>
            <div class="column2">
                <div id="answer_exp"></div>
            </div>
            </div>
            <div class="row">
            <div class="column1">
            <div id="languages">
                <strong>Millised tarkvaraarendamise keeled te teate?</strong>
                <br>
                <br>
                <input type="checkbox" name="lang" id="lang1" value="JavaScript" onchange="languages()">
                <label for="lang1">JavaScript</label>
                <input type="checkbox" name="lang" id="lang2" value="Python" onchange="languages()">
                <label for="lang2">Python</label>
                <input type="checkbox" name="lang" id="lang3" value="PHP" onchange="languages()">
                <label for="lang3">PHP</label>
                <input type="checkbox" name="lang" id="lang4" value="C#" onchange="languages()">
                <label for="lang4">C#</label>
            </div>
            </div>
            <div class="column2"><div id="answer_lang"></div></div>
            </div>
            <div class="row">
            <div class="column1">
            <div id="salary">
                <strong><label>Mis palka tahaksite saada?</label></strong>
                <select id="sal" onchange="salary()">
                    <option value="">...</option>
                    <option value="1000-2000$">1000-2000$</option>
                    <option value="2000-4000$">2000-4000$</option>
                    <option value="5000$+">5000$+</option>
                </select>
            </div>
            </div>
            <div class="column2"><div id="answer_salary"></div></div>
            </div>
            <div id="final">
                <input type="button" value="Loe andmed" onclick="read_data()">
                <input type="reset" value="Puhasta" onclick="deletes()">
            </div>
            <div id="answer_final"></div>
        </div>
        </div>
</form>        
</body>
</html>