
let input = document.getElementById("nameInput");


let form = document.getElementById("myForm");


form.addEventListener("reset", function(e) {
  e.preventDefault(); // stops page reload
  alert("Form Successfully Submitted!");
});