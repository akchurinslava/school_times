   <head>
        <meta charset="UTF-8">
        <title>JS katsed</title>
        <script src="js/form_script3.js"></script>
    </head>
        <br>
        <div id="vastus2"></div>
        <h1>SISETA KOGUS JA VALI VALUUTA</h1>
        <form name="var1" id="var1">
        <table>
            <caption>Valuuta kalkulaator</caption>
            <tr>
                <td>
                    <br>
                    <input type="radio" name="valuuta" id="dollar" value="dollar" onchange="radioChange(event)">
                    <label for="dollar">Dollar</label>
                    <br>
                    <input type="radio" name="valuuta" id="rub" value="rub" onchange="radioChange(event)">
                    <label for="rub">Rub</label>
                    <br>
                    <input type="radio" name="valuuta" id="kroon" value="kroon" onchange="radioChange(event)">
                    <label for="kroon">Sek</label>
                    <br>
                    <input type="radio" name="valuuta" id="frank" value="frank" onchange="radioChange(event)">
                    <label for="frank">Frank</label>
                    <br>
                </td>
                <td class="centr">
                    <label for="valik">Vali valuuta:</label>
                    <select id="valik" onchange="selectOptionChange(event)">
                        <option>...vali...</option>
                        <option value="dollar">Dollar</option>
                        <option value="rub">Rub</option>
                        <option value="kroon">Sek</option>
                        <option value="frank">Frank</option>
                    </select>
                </td>
                <td>
                    <input type="text" id="mark4" name="mark4" oninput="m4()">
                </td>
                <td>
                    <input type="checkbox" name="currency" id="currency1" value="dollar" onchange="mycheckbox()">
                    <label for="currency1">Dollar</label>
                    <br>
                    <input type="checkbox" name="currency" id="currency2" value="rub" onchange="mycheckbox()">
                    <label for="currency2">Rub</label>
                    <br>
                    <input type="checkbox" name="currency" id="currency3" value="kroon" onchange="mycheckbox()">
                    <label for="currency3">Sek</label>
                    <br>
                    <input type="checkbox" name="currency" id="currency4" value="frank" onchange="mycheckbox()">
                    <label for="currency4">Frank</label>
                </td>
            </tr>
            <tr class="centr">
                <td colspan="4">
                <label for="kogus">Kogus:</label>
                <input type="text" id="kogus" name="kogus" oninput="input_change()">
                <div id="vastus"></div>
                <div id="object">
                <input type="button" value="OK" onclick="validateForm()">
                <input type="reset" value="Puhasta" onclick="puhasta_delete()">
                </div>
                </td>
            </tr>
        </table>
    </form>
    </div>
    </div>
    </body>