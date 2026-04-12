
    function loadJobs() {
        const tableBody = document.getElementById('jobsTableBody');
        
        const jobs = JSON.parse(localStorage.getItem('myJobs')) || [];

        if (jobs.length === 0) {
            tableBody.innerHTML = '<tr><td colspan="6">No jobs added yet by admin.</td></tr>';
            return;
        }

        tableBody.innerHTML = jobs.map(job => `
            <tr>
                <td>${job.title}</td>
                <td>${job.company}</td>
                <td>${job.salary}</td>
                <td>${job.ExperienceRequired}</td>
                <td class="status-cell"><mark>${job.status}</mark></td>
                <td><button onclick="applyJob(this, '${job.id}')">Apply</button></td>
            </tr>
        `).join('');
    }

    function applyJob(button, jobId) {
        alert('Applied for Job ID: ' + jobId);
        button.innerText = 'Applied';
        button.disabled = true;
        const row = button.closest('tr');
        row.querySelector('.status-cell').innerHTML = '<span class="closed">Closed</span>';
    }

    loadJobs();