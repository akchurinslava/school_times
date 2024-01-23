const dollar=1.16;
const sek=10.65;
const rub=84.20;
const frank=1.077;

function randompic(){
    const images = [
      '/Users/my_pc/Library/Mobile Documents/com~apple~CloudDocs/iCloud Drive/work/programming/github/html_css/forms3/man.png',
      '/Users/my_pc/Library/Mobile Documents/com~apple~CloudDocs/iCloud Drive/work/programming/github/html_css/forms3/no.png',
      '/Users/my_pc/Library/Mobile Documents/com~apple~CloudDocs/iCloud Drive/work/programming/github/html_css/forms3/woman.png'
    ];
    const randomIndex = Math.floor(Math.random() * images.length);
    const randomImage = images[randomIndex];
    
    const img = document.getElementById('random-img');
    img.src = randomImage;
}

function imgChoice(){
    const img = document.getElementById('random-img');
    if(document.getElementById("valik5").value==img.getAttribute("src"))
    {
        document.getElementById("vastus2").innerHTML="õige";
    }
    else{
        document.getElementById("vastus2").innerHTML="vale";   
    }
     
}

function tyhistaRadioValik(){
  var elem=document.getElementsByName("valuuta");
  for(var i=0; i<elem.length; i++){
    elem[i].checked=false; 
    }
}

function tyhistavastus(){
    let vastus=document.getElementById("vastus");
    vastus.textContent = " ";
}

function tyhistaCheckboxValik(){
    var elem=document.getElementsByName("valik2");
    for(var i=0; i<elem.length; i++){
      elem[i].checked=false; 
    }
}

function tyhistaselectOptionChange(){
    let select_valik = document.getElementById("valik");
    select_valik.selectedIndex = 0;
    
}

function validateForm() {
    let x = document.forms["var1"]["kogus"].value;
    if (x == "") {
        alert("Sisesta kogus! ");
        return false;
    }
}

function tyhistamycheckbox(){
    let curr1 = document.getElementById("currency1");
    let curr2 = document.getElementById("currency2");
    let curr3 = document.getElementById("currency3");
    let curr4 = document.getElementById("currency4");
    curr1.disabled = false;
    curr2.disabled = false;
    curr3.disabled = false;
    curr4.disabled = false;
}

function calculate(val, currency){
    return (val*currency).toFixed(2);
 
}

function deleteinput(){
    input = document.getElementById("kogus");
    input.value = "";
}

function puhasta_delete(){
    let vastus=document.getElementById("vastus");
    vastus.textContent = " ";
    var elem = document.getElementsByName("currency");
    for(var i=0; i<elem.length; i++){
      elem[i].checked=false;
      elem[i].disabled=false; 
    }
}


function radioChange(event) {
    puhasta_delete();
    let vastus=document.getElementById("vastus");
    let kogus=document.getElementById("kogus");
    let inputValue=kogus.value;
        if (event.target.id === "dollar") {
            vastus.innerHTML = calculate(inputValue, dollar) + " $";
        } else if (event.target.id === "rub") {
            vastus.innerHTML = calculate(inputValue, rub) + " ₽";
        } else if (event.target.id === "kroon") {
            vastus.innerHTML = calculate(inputValue, sek) + " SEK";
        } else if (event.target.id === "frank") {
            vastus.innerHTML = calculate(inputValue, frank) + " CHF";
        }
}

function selectOptionChange(event){
    tyhistaRadioValik();
    puhasta_delete();
    let vastus=document.getElementById("vastus");
    let kogus=document.getElementById("kogus");
    let inputValue=kogus.value;
    if (event.target.value === "dollar") {
        vastus.innerHTML = calculate(inputValue, dollar) + " $";
    } else if (event.target.value === "rub") {
        vastus.innerHTML = calculate(inputValue, rub) + " ₽";
    } else if (event.target.value === "kroon") {
        vastus.innerHTML = calculate(inputValue, sek) + " SEK";
    } else if (event.target.value === "frank") {
        vastus.innerHTML = calculate(inputValue, frank) + " CHF";
    }
}

function mycheckbox(){
    tyhistaRadioValik();
    tyhistaselectOptionChange();
    tyhistavastus();
    let sym = "";
    let curr1 = document.getElementById("currency1");
    let curr2 = document.getElementById("currency2");
    let curr3 = document.getElementById("currency3");
    let curr4 = document.getElementById("currency4");
    j = 0;
    if (curr1.checked){
        j = dollar;
        sym = "$";
        curr2.disabled = true;
        curr3.disabled = true;
        curr4.disabled = true;
    }
    else if(curr2.checked){
        j = rub;
        sym = "₽";
        curr1.disabled = true;
        curr3.disabled = true;
        curr4.disabled = true;
    }
    else if(curr3.checked){
        j = sek;
        sym = "SEK";
        curr1.disabled = true;
        curr2.disabled = true;
        curr4.disabled = true;
    }
    else if(curr4.checked){
        j = frank;
        sym = "CHF";
        curr1.disabled = true;
        curr2.disabled = true;
        curr3.disabled = true;
    }
    else{
        curr1.disabled = false;
        curr2.disabled = false;
        curr3.disabled = false;
        curr4.disabled = false;
        

    }
    return { x: j, y: sym };

}

function input_change(){
    let values = mycheckbox();
    let x = values.x;
    let y = values.y;
    let inpt = document.getElementById("kogus");
    let vastus = document.getElementById("vastus");
    vastus.textContent = (inpt.value * x).toFixed(2) + " " + y;
}

function m4(){
    tyhistaRadioValik();
    tyhistaselectOptionChange();
    tyhistavastus();
    tyhistamycheckbox();
    puhasta_delete();
    let name = document.getElementById("mark4");
    let vastus = document.getElementById("vastus");
    let inputValue=kogus.value;
    if (name.value == "dollar") {
        vastus.textContent = calculate(inputValue, dollar) + " $";
    }
    else if (name.value === "rub") {
        vastus.textContent = calculate(inputValue, rub) + " ₽";
    }
    else if (name.value === "kroon") {
        vastus.textContent = calculate(inputValue, sek) + " SEK";
    }
    else if (name.value === "frank") {
        vastus.textContent= calculate(inputValue, frank) + " CHF";
    }
    else{
        vastus.textContent = " ";
    }

}