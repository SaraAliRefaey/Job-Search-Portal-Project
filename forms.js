function validatePassword(){
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('Confirmp').value;
    if (password !== confirmPassword){
        alert("Passwords do NOT match");
        return false;
    }
    return true;
}

function showCompanyName(){
    var isChecked = document.getElementById('companyadmin').checked;
    var companyName = document.getElementById('company');
    var label = document.getElementById('companyLabel');
    if (isChecked == true){
        companyName.hidden = false;
        label.hidden = false;
    }
    else {
        companyName.hidden = true;
        label.hidden = true;
    }
}

var showIcon1 = document.getElementById("show-password");
var password = document.getElementById("password");
function showPassword(){
    if (password.type === "password"){
        password.type = "text";
    }
    else {
        password.type = "password";
    }
}
showIcon1.addEventListener("click", showPassword);

var showIcon2 = document.getElementById("show-confirm-password");
var confirm = document.getElementById("Confirmp");
function showConfirmPassword(){
    if (confirm.type === "password"){
        confirm.type = "text";
    }
    else {
        confirm.type = "password";
    }
}
showIcon2.addEventListener("click", showConfirmPassword);