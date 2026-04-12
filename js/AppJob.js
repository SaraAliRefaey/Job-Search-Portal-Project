/* ============================================================
   Applied Jobs Page - Functionality (Local Storage)
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
    // Initializing mock data if Local Storage is empty
    initializeMockData();
    
    // Display the jobs on page load
    displayAppliedJobs();

    // Event listener for search/filter input
    const searchInput = document.querySelector('input[type="search"]');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            filterJobs(e.target.value);
        });
    }
});

/**
 * Initializes Local Storage with dummy data if it's the first time running
 */
function initializeMockData() {
    const existingData = localStorage.getItem('appliedJobs');
    if (!existingData) {
        const dummyApplications = [
            { id: 1, title: 'Frontend Developer', company: 'Tech Solutions', date: '2023-10-01', status: 'accepted' },
            { id: 2, title: 'UI/UX Designer', company: 'Creative Agency', date: '2023-10-05', status: 'pending' },
            { id: 3, title: 'Backend Engineer', company: 'Data Systems', date: '2023-10-08', status: 'rejected' }
        ];
        localStorage.setItem('appliedJobs', JSON.stringify(dummyApplications));
    }
}

/**
 * Fetches data from Local Storage and renders it into the table
 */
function displayAppliedJobs(filterText = '') {
    const tableBody = document.getElementById('appliedJobsList');
    const applications = JSON.parse(localStorage.getItem('appliedJobs')) || [];
    
    // Clear the table before re-rendering
    tableBody.innerHTML = '';

    const filteredApps = applications.filter(app => 
        app.title.toLowerCase().includes(filterText.toLowerCase()) ||
        app.company.toLowerCase().includes(filterText.toLowerCase())
    );

    if (filteredApps.length === 0) {
        tableBody.innerHTML = `<tr><td colspan="4" style="text-align:center;">No applications found.</td></tr>`;
        return;
    }

    filteredApps.forEach(app => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${app.title}</td>
            <td>${app.company}</td>
            <td>${app.date || 'N/A'}</td>
            <td><span class="status-badge status-${app.status}">${app.status.toUpperCase()}</span></td>
            <td>
                <button class="btn-withdraw" onclick="withdrawApplication(${app.id})">
                    <i class="fa-solid fa-trash-can"></i> Withdraw
                </button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

/**
 * Filters the table rows based on user input
 */
function filterJobs(query) {
    displayAppliedJobs(query);
}

/**
 * Deletes an application from Local Storage and updates the UI
 */
window.withdrawApplication = function(id) {
    if (confirm('Are you sure you want to withdraw this application?')) {
        let applications = JSON.parse(localStorage.getItem('appliedJobs')) || [];
        applications = applications.filter(app => app.id !== id);
        
        localStorage.setItem('appliedJobs', JSON.stringify(applications));
        displayAppliedJobs(); // Refresh the table
    }
};
