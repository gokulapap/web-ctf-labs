var attempt = 10;

function validate(){
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
if ( username == "nasa_hamcker" && password == "cringe_hamcker"){
alert ("one click suvar broken !!!!!!");
window.location = "ppthacker"; // Redirecting to other page.
return false;
}
else{
attempt --;// Decrementing by one.
alert("You have only left "+attempt+" attempt!");

// Disabling fields after 10 attempts
if( attempt == 0){
alert("soli mudinchu avlo daan")
document.getElementById("username").disabled = true;
document.getElementById("password").disabled = true;
document.getElementById("submit").disabled = true;
return false;
}
}
}
