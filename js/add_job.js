myform=document.querySelector("form");
myform.addEventListener("submit",function(event){
event.preventDefault();
const title=document.getElementById("title").value;
const company= document.getElementById('company').value,
const salary=document.getElementById("salary").value;
const ExperienceRequired= document.getElementById('experience required').value,
const description=document.getElementById("description").value;
const status=document.getElementById("status").value;

if(title==""){
document.getElementById("tit").style.display='block' ;
return;
}
if(salary==""){
document.getElementById("sal").style.display='block' ;
return;
}
if(description==""){
document.getElementById("des").style.display='block' ;
return;
}

if (title.length<5){
     alert("Job title must be at least 5 characters");
        return;
}

 if (salary <= 1000) {
        alert("Please Enter Valid Salary");
        return;
    }
 if (description.length < 10) {
        alert("Description must be at least 10 characters");
        return;
    }
   
const job ={
id:Date.now(),
title:title,
company:company,
salary:salary,
ExperinceRequired:ExperienceRequired,
description:description,
status:status};

let jobs = JSON.parse(localStorage.getItem("jobs")) || [];
jobs.push(job);

localStorage.setItem("jobs", JSON.stringify(jobs));

alert("Job added successfully!");

myform.reset();




})
const titleInput = document.getElementById("title");
const titleError = document.getElementById("tit");
titleInput.addEventListener("input", function() {
    if (titleInput.value.trim() !== "") {
        titleError.style.display = "none";
    }
});

const salaryInput = document.getElementById("salary");
const salaryError = document.getElementById("sal");

salaryInput.addEventListener("input", function() {
    if (salaryInput.value !== "") {
        salaryError.style.display = "none";
    }
});
const descInput = document.getElementById("description");
const descError = document.getElementById("des");

descInput.addEventListener("input", function() {
    if (descInput.value.trim() !== "") {
        descError.style.display = "none";
    }
});




