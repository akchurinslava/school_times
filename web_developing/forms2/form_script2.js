
function name_abs(){
    let name1 = document.getElementById("name1");
    answer_name.innerHTML = "Tere "+name1.value+"!";
    return answer_name.innerHTML;
}




function deletes(){
    let answer = document.getElementById("answer_final");
    let answer_name = document.getElementById("answer_name");
    let answer_age = document.getElementById("answer_age");
    let answer_exp = document.getElementById("answer_exp");
    let answer_lang = document.getElementById("answer_lang");
    let answer_salary = document.getElementById("answer_salary");
    answer.innerHTML="";
    answer_name.innerHTML="";
    answer_age.innerHTML="";
    answer_exp.innerHTML="";
    answer_lang.innerHTML="";
    answer_salary.innerHTML="";
    answer_final.innerHTML="";
    let exp = null;
    let age = null;
    value.textContent = 50;
}


function salary(){
    let salary = document.getElementById("sal")
    let answer_salary = document.getElementById("answer_salary");

    if(sal.selectedIndex!=0){
        answer_salary.innerHTML="Te valisite "+salary.value+" palka";
        answer_salary.style.color="#f0eff6";

    } else{
        answer_salary.innerHTML="Palun vali oma oodatava palka";
        answer_salary.style.color="red";
    }
    return answer_salary.innerHTML;
}

function languages(){
    let name = document.getElementById("name1");
    let answer_lang = document.getElementById("answer_lang");
    let lang1 = document.getElementById("lang1");
    let lang2 = document.getElementById("lang2");
    let lang3 = document.getElementById("lang3");
    let lang4 = document.getElementById("lang4");

    var lang = "";
    if(lang1.checked){
        lang+=lang1.value+", ";
    }
    if(lang2.checked){
        lang+=lang2.value+", ";
    }
    if(lang3.checked){
        lang+=lang3.value+", ";
    }
    if(lang4.checked){
        lang+=lang4.value+" ";
    }
    if(lang==""){
        lang="sa ei valinud tarkvaraarendamis keelt";
        lang.style.color="red";
    }
    answer_lang.innerHTML="Teie valikud: "+lang;
    return answer_lang.innerHTML;

}

function level(){
    let years1_2 = document.getElementById("1-2years");
    let years2_5 = document.getElementById("2-5years");
    let years5_10 = document.getElementById("5-10years");
    let years10 = document.getElementById("10+years");
    if(years1_2.checked){
        exp = years1_2.value;
    } else if(years2_5.checked){
        exp = years2_5.value;
    }
    else if(years5_10.checked){
        exp = years5_10.value;
    }
    else if(years10.checked){
        exp = years10.value;
    }
    else{
        exp = "sa ei valinud";
    }
    answer_exp.innerHTML = "Teie kogemus on, " +exp;
    return answer_exp.innerHTML;
}

function range_form(){
    answer_age.innerHTML = "Teie vanus on " +value.value + " a.";
    return answer_age.innerHTML
}

function read_data(){
    if(answer_name.innerHTML == "" || answer_age.innerHTML == "" || answer_exp.innerHTML == "" || answer_lang.innerHTML == "" || answer_salary.innerHTML == ""){
        answer_final.innerHTML = "You must enter all data";
    }
    else{
    answer_final.innerHTML = name_abs()+" " + range_form()+" " + level()+". " + languages()+"." + salary()+"!";
    }
}