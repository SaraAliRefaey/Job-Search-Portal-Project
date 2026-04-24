let jobs = JSON.parse(localStorage.getItem("workwave_jobs")) || [
  {
    id: 1,
    title: "Software Engineer",
    company: "Google",
    salary: "196$",
    experience: 3,
    status: "Open",
  },
  {
    id: 2,
    title: "Front-end Developer",
    company: "Bosta",
    salary: "25k",
    experience: 1,
    status: "Open",
  },
];

// const roleBtn = document.getElementById("btn");
// const roleText = document.getElementById("role-text");
const addJobSection = document.getElementById("add-job-section");
const jobsContainer = document.getElementById("jobs-container");
const addJobForm = document.getElementById("add-job-form");
const searchForm = document.querySelector("#search-form");

function renderJobs(data) {
  jobsContainer.innerHTML = "";
  data.forEach((job) => {
    const card = `
        <div class="job-card">
    <h4>${job.title}</h4>
    <p><i class="fa fa-building"></i> ${job.company} </p>
    <p><i class="fa fa-briefcase"></i> Exp : ${job.experience}</p>
    <p class="salary">${job.salary}</p>
    <span class="badge">${job.status}</span>
    <div class="card-footer">
        <button class="apply-btn" onclick="alert('Applied!')"> Apply </button>
        <button class="delete-btn" onclick="deleteJob(${job.id})"><i class="fa fa-trash"></i></button>
    </div>
</div>`;

    jobsContainer.innerHTML += card;
  });
}

// roleBtn.addEventListener("click" , () => {

//     const isAdmin = addJobSection.classList.toggle("hidden");
//     roleText.innerText = isAdmin ? " Switch Admin" : " Switch User";
//     localStorage.setItem("role" , isAdmin ? "user" : "admin");
// });

addJobForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const newJob = {
    id: Date.now(),
    title: document.getElementById("new-title").ariaValueMax,
    company: document.getElementById("new company").ariaValueMax,
    salary: document.getElementById("new-salary").ariaValueMax,
    experience: parseInt(document.getElementById("new-exp").value),
    status: "Open",
  };
  jobs.push(newJob);
  saveAndRender();
  addJobForm.reset();
});

searchForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const titleQuery = document.getElementById("job-title").value.toLowerCase();
  const expQuery = parseInt(document.getElementById("experience").value) || 0;

  localStorage.setItem("search_title", titleQuery);
  localStorage.setItem("search_experience", expQuery);
//   const filtered = jobs.filter( job =>
//       job.title.toLowerCase().includes(titleQuery) && job.experience >= expQuery
//   );

//   renderJobs(filtered);

  window.location.href = "job-details.html";
});

function deleteJob(id) {
  jobs = jobs.filter((job) => job.id !== id);
  saveAndRender();
}

function saveAndRender() {
  localStorage.setItem("workwave_jobs", JSON.stringify(jobs));
  renderJobs(jobs);
}

renderJobs(jobs);

addJobSection.classList.add("hidden");

const userRole = localStorage.getItem("role");

const adminLink = document.getElementById("admin-dashboard-link");

if (userRole === "admin") {
  addJobSection.classList.remove("hidden");

  if (adminLink) {
    adminLink.style.display = "inline-block";
  }
} 
  else {
    addJobSection.classList.add("hidden");
  }

