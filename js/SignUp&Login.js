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
const isShowIcon2 = document.getElementById("show-confirm-password");
const isConfirm = document.getElementById("Confirmp");
function showConfirmPassword(){
    if (confirm.type === "password"){
        confirm.type = "text";
    }
    else {
        confirm.type = "password";
    }
}
if (isShowIcon2 && isConfirm){
    showIcon2.addEventListener("click", showConfirmPassword);
}





// Login system using local storage
const loginForm = document.getElementById("loginForm");
if (loginForm){
    loginForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        const user = localStorage.getItem(username);

        if(user){
            const parsedUser = JSON.parse(user);
            if(parsedUser.password === password){
                localStorage.setItem("user", JSON.stringify(parsedUser));
                
                if (parsedUser.isAdmin){
                    window.location.href = "index.html";
                }
                else{
                    window.location.href = "Recruiter dashboard.html";
                }

            }
            else {
                alert("Incorrect password");
            }
        }
        else {
            alert("User not found");
        }
    });
}


// Sign up system using local storage    
const signupForm = document.getElementById("signUpForm");
if(signupForm){
    signupForm.addEventListener("submit", function(event){
        event.preventDefault();
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        const confirmPassword = document.getElementById("Confirmp").value;
        const isAdmin = document.getElementById("admin").checked;

        if (password !== confirmPassword){
            return;
        }

        const user = {
            username: username,
            password: password,
            isAdmin: isAdmin,
        };

        localStorage.setItem(username, JSON.stringify(user));
        alert("Registration successful! Please login.");
        window.location.href = "Login.html";
    });
}
