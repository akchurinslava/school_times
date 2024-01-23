import "./styles.css";


function getXMLconsole(){
  let xmlhttp = new XMLHttpRequest
  console.log(xmlhttp);
  xmlhttp.open("GET", "src/games.xml", false);
  xmlhttp.send();
  console.log(xmlhttp.responseXML);
}

function getXML(){
  let xmlhttp = new XMLHttpRequest();
  console.log(xmlhttp);
  xmlhttp.open("GET", "src/games.xml", false);
  console.log(xmlhttp);
  xmlhttp.send();
  let XMLContent = xmlhttp.responseXML;
  console.log(xmlhttp.responseXML);
  let tableRows = 
  "<tr><th>Title</th><th>Price</th></tr>";
  let gameElements = XMLContent.getElementsByTagName("game");
  for (let i = 0; i < gameElements.length; i++){
    tableRows +=
    "<tr><td>" +
    gameElements[i].getElementsByTagName("title")[0].childNodes[0].nodeValue + 
    "</td><td>" +
    gameElements[i].getElementsByTagName("price")[0].childNodes[0].nodeValue + 
    "</td><tr>"
  }
  document.getElementById("xmlTable").innerHTML = tableRows;
}
document.getElementById("app").innerHTML = `
<table id="xmlTable"></table>
`;

getXMLconsole();
getXML();