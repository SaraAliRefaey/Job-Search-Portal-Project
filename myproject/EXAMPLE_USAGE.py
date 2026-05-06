"""
Job Search Website Backend - Example Usage & Testing Guide

This file contains example code and cURL commands to test the API
"""

# ============================================================================
# SECTION 1: PYTHON REQUESTS EXAMPLES
# ============================================================================

import requests
import json

BASE_URL = "http://localhost:8000/api"

# Example 1: Register a Regular User
# ============================================================================
def register_regular_user():
    """Register a new regular user"""
    url = f"{BASE_URL}/register/"
    data = {
        "username": "john_doe",
        "email": "john@example.com",
        "password": "securepassword123",
        "is_company_admin": False
    }
    response = requests.post(url, json=data)
    print("Register Regular User:")
    print(response.json())
    return response.json()


# Example 2: Register a Company Admin
# ============================================================================
def register_company_admin():
    """Register a new company admin"""
    url = f"{BASE_URL}/register/"
    data = {
        "username": "acme_admin",
        "email": "admin@acme.com",
        "password": "securepassword123",
        "is_company_admin": True,
        "company_name": "ACME Corporation"
    }
    response = requests.post(url, json=data)
    print("Register Company Admin:")
    print(response.json())
    return response.json()


# Example 3: Login and Get JWT Tokens
# ============================================================================
def login(username, password):
    """Login and get JWT access and refresh tokens"""
    url = f"{BASE_URL}/login/"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, json=data)
    tokens = response.json()
    print("Login Response:")
    print(json.dumps(tokens, indent=2))
    return tokens


# Example 4: Create a Job (Admin Only)
# ============================================================================
def create_job(access_token, title, salary, company_name, description, years_of_experience):
    """Create a new job posting (Admin only)"""
    url = f"{BASE_URL}/jobs/"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "title": title,
        "salary": salary,
        "company_name": company_name,
        "status": "open",
        "description": description,
        "years_of_experience": years_of_experience
    }
    response = requests.post(url, json=data, headers=headers)
    print("Create Job Response:")
    print(json.dumps(response.json(), indent=2))
    return response.json()


# Example 5: List All Jobs
# ============================================================================
def list_jobs(access_token):
    """Get list of all open jobs"""
    url = f"{BASE_URL}/jobs/"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    print("List Jobs Response:")
    print(json.dumps(response.json(), indent=2))
    return response.json()


# Example 6: Search Jobs
# ============================================================================
def search_jobs(access_token, title=None, experience=None):
    """Search for jobs by title and/or experience"""
    url = f"{BASE_URL}/jobs/search/"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {}
    if title:
        params["title"] = title
    if experience:
        params["experience"] = experience
    
    response = requests.get(url, params=params, headers=headers)
    print("Search Jobs Response:")
    print(json.dumps(response.json(), indent=2))
    return response.json()


# Example 7: Get Job Details
# ============================================================================
def get_job_details(access_token, job_id):
    """Get details of a specific job"""
    url = f"{BASE_URL}/jobs/{job_id}/"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    print(f"Get Job {job_id} Response:")
    print(json.dumps(response.json(), indent=2))
    return response.json()


# Example 8: Update a Job (Admin Owner Only)
# ============================================================================
def update_job(access_token, job_id, title=None, salary=None, status=None, description=None):
    """Update a job posting (Owner only)"""
    url = f"{BASE_URL}/jobs/{job_id}/"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {}
    if title:
        data["title"] = title
    if salary:
        data["salary"] = salary
    if status:
        data["status"] = status
    if description:
        data["description"] = description
    
    response = requests.put(url, json=data, headers=headers)
    print(f"Update Job {job_id} Response:")
    print(json.dumps(response.json(), indent=2))
    return response.json()


# Example 9: Delete a Job (Admin Owner Only)
# ============================================================================
def delete_job(access_token, job_id):
    """Delete a job posting (Owner only)"""
    url = f"{BASE_URL}/jobs/{job_id}/"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.delete(url, headers=headers)
    print(f"Delete Job {job_id} Response:")
    print(f"Status Code: {response.status_code}")
    if response.text:
        print(json.dumps(response.json(), indent=2))
    return response.status_code


# Example 10: Apply for a Job
# ============================================================================
def apply_for_job(access_token, job_id):
    """Apply for a specific job"""
    url = f"{BASE_URL}/applications/"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {"job": job_id}
    response = requests.post(url, json=data, headers=headers)
    print(f"Apply for Job {job_id} Response:")
    print(json.dumps(response.json(), indent=2))
    return response.json()


# Example 11: Get My Applications
# ============================================================================
def get_my_applications(access_token):
    """Get list of all applications made by current user"""
    url = f"{BASE_URL}/applications/"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    print("My Applications Response:")
    print(json.dumps(response.json(), indent=2))
    return response.json()


# Example 12: Get Admin's Jobs
# ============================================================================
def get_admin_jobs(access_token):
    """Get all jobs created by the admin user"""
    url = f"{BASE_URL}/jobs/admin_jobs/"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    print("Admin Jobs Response:")
    print(json.dumps(response.json(), indent=2))
    return response.json()


# ============================================================================
# SECTION 2: COMPLETE WORKFLOW EXAMPLE
# ============================================================================

def run_complete_workflow():
    """Run a complete workflow demonstrating the API"""
    print("\n" + "="*80)
    print("COMPLETE WORKFLOW EXAMPLE")
    print("="*80 + "\n")

    # Step 1: Register users
    print("STEP 1: REGISTER USERS")
    print("-" * 80)
    admin_data = register_company_admin()
    print()
    user_data = register_regular_user()
    print()

    # Step 2: Login
    print("STEP 2: LOGIN")
    print("-" * 80)
    admin_tokens = login("acme_admin", "securepassword123")
    admin_token = admin_tokens["access"]
    print()
    user_tokens = login("john_doe", "securepassword123")
    user_token = user_tokens["access"]
    print()

    # Step 3: Admin creates jobs
    print("STEP 3: ADMIN CREATES JOBS")
    print("-" * 80)
    job1 = create_job(
        admin_token,
        "Senior Python Developer",
        "120000.00",
        "ACME Corporation",
        "Looking for an experienced Python developer with 5+ years of experience",
        5
    )
    job1_id = job1["id"]
    print()
    
    job2 = create_job(
        admin_token,
        "Junior Web Developer",
        "60000.00",
        "ACME Corporation",
        "Looking for a junior web developer with 1-2 years of experience",
        1
    )
    job2_id = job2["id"]
    print()

    # Step 4: List jobs
    print("STEP 4: LIST ALL JOBS")
    print("-" * 80)
    jobs = list_jobs(user_token)
    print()

    # Step 5: Search jobs
    print("STEP 5: SEARCH JOBS")
    print("-" * 80)
    search_results = search_jobs(user_token, title="python", experience=5)
    print()

    # Step 6: Get job details
    print("STEP 6: GET JOB DETAILS")
    print("-" * 80)
    job_details = get_job_details(user_token, job1_id)
    print()

    # Step 7: User applies for jobs
    print("STEP 7: USER APPLIES FOR JOBS")
    print("-" * 80)
    application1 = apply_for_job(user_token, job1_id)
    print()
    application2 = apply_for_job(user_token, job2_id)
    print()

    # Step 8: Get user's applications
    print("STEP 8: GET USER'S APPLICATIONS")
    print("-" * 80)
    my_apps = get_my_applications(user_token)
    print()

    # Step 9: Admin views their jobs
    print("STEP 9: ADMIN VIEWS THEIR JOBS")
    print("-" * 80)
    admin_jobs = get_admin_jobs(admin_token)
    print()

    # Step 10: Admin closes a job
    print("STEP 10: ADMIN CLOSES A JOB")
    print("-" * 80)
    update_job(admin_token, job1_id, status="closed")
    print()

    # Step 11: Try to apply to closed job (should fail)
    print("STEP 11: TRY TO APPLY TO CLOSED JOB (SHOULD FAIL)")
    print("-" * 80)
    try:
        apply_for_job(user_token, job1_id)
    except Exception as e:
        print(f"Error (expected): {e}")
    print()

    print("="*80)
    print("WORKFLOW COMPLETE")
    print("="*80)


# ============================================================================
# SECTION 3: CURL COMMANDS
# ============================================================================

"""
# Register Regular User
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "is_company_admin": false
  }'

# Register Company Admin
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "acme_admin",
    "email": "admin@acme.com",
    "password": "securepassword123",
    "is_company_admin": true,
    "company_name": "ACME Corporation"
  }'

# Login
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "securepassword123"
  }'

# List Jobs
curl -X GET http://localhost:8000/api/jobs/ \
  -H "Authorization: Bearer <access_token>"

# Search Jobs
curl -X GET "http://localhost:8000/api/jobs/search/?title=python&experience=5" \
  -H "Authorization: Bearer <access_token>"

# Get Job Details
curl -X GET http://localhost:8000/api/jobs/1/ \
  -H "Authorization: Bearer <access_token>"

# Create Job (Admin Only)
curl -X POST http://localhost:8000/api/jobs/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Senior Python Developer",
    "salary": "120000.00",
    "company_name": "ACME Corporation",
    "status": "open",
    "description": "Looking for an experienced Python developer...",
    "years_of_experience": 5
  }'

# Update Job (Admin Owner Only)
curl -X PUT http://localhost:8000/api/jobs/1/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "closed"
  }'

# Delete Job (Admin Owner Only)
curl -X DELETE http://localhost:8000/api/jobs/1/ \
  -H "Authorization: Bearer <access_token>"

# Apply for Job
curl -X POST http://localhost:8000/api/applications/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"job": 1}'

# Get My Applications
curl -X GET http://localhost:8000/api/applications/ \
  -H "Authorization: Bearer <access_token>"

# Get Admin's Jobs
curl -X GET http://localhost:8000/api/jobs/admin_jobs/ \
  -H "Authorization: Bearer <access_token>"
"""


# ============================================================================
# SECTION 4: MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Make sure to run this after the server is running:
    # python manage.py runserver
    
    try:
        run_complete_workflow()
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to the API server.")
        print("Make sure to run: python manage.py runserver")
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
