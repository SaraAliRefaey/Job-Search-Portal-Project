"use strict";

window.onload = function() 
{
    displayJobs();
};

function displayJobs() {
   
    var jobs = JSON.parse(localStorage.getItem("jobs")) || [];
    var tableBody = document.getElementById("jobsTableBody");

     
    tableBody.innerHTML = ""; 

    if (jobs.length === 0) {
        jobs = [
            { title: "Front-end Developer", salary: "15,000", status: "Open" },
            { title: "Python Developer", salary: "25,000", status: "Closed" }
        ];
        localStorage.setItem("jobs", JSON.stringify(jobs));
    }

             for (var i = 0; i < jobs.length; i++) {
        var row = "<tr>" +
            "<td>" + jobs[i].title + "</td>" +
            "<td>" + jobs[i].salary + " EGP</td>" +
            "<td>" + jobs[i].status + "</td>" +
            "<td>" +
                "<a href='edit_job.html' class='btn-edit'>Edit</a> " +
                "<button class='btn-delete' onclick='deleteJob(" + i + ")'>Delete</button>" +
            "</td>" +
        "</tr>";
        tableBody.innerHTML += row;
    }
}



function deleteJob(index)
 {
    if (confirm("Are you Sure to Delete This Job?")) {
        var jobs = JSON.parse(localStorage.getItem("jobs")) || [];
        
    
        jobs.splice(index, 1);
        
      localStorage.setItem("jobs", JSON.stringify(jobs));
        
        displayJobs();
        
        alert("Job deleted permanently!");
    }
}