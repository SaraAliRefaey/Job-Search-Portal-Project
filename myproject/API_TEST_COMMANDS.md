# Job Search Website Backend - API Testing Commands

## Quick Start (Run these commands in order)

### 1. START THE SERVER
```bash
python manage.py runserver
```
Server will start at http://localhost:8000/api/

---

## TESTING WORKFLOW

### Step 1: Register a Regular User
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "is_company_admin": false
  }'
```

**Expected Response (201):**
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "is_company_admin": false,
  "company_name": null
}
```

---

### Step 2: Register a Company Admin
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "acme_admin",
    "email": "admin@acme.com",
    "password": "securepassword123",
    "is_company_admin": true,
    "company_name": "ACME Corporation"
  }'
```

**Expected Response (201):**
```json
{
  "id": 2,
  "username": "acme_admin",
  "email": "admin@acme.com",
  "is_company_admin": true,
  "company_name": "ACME Corporation"
}
```

---

### Step 3: Login as Regular User
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "securepassword123"
  }'
```

**Expected Response (200):**
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Save the access token!** Use it as: `<user_token>`

---

### Step 4: Login as Company Admin
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "acme_admin",
    "password": "securepassword123"
  }'
```

**Save the access token!** Use it as: `<admin_token>`

---

### Step 5: Create a Job (Admin Only)
```bash
curl -X POST http://localhost:8000/api/jobs/ \
  -H "Authorization: Bearer <admin_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Senior Python Developer",
    "salary": "120000.00",
    "company_name": "ACME Corporation",
    "status": "open",
    "description": "Looking for an experienced Python developer with 5+ years of experience. Must have experience with Django and REST APIs.",
    "years_of_experience": 5
  }'
```

**Expected Response (201):**
```json
{
  "id": 1,
  "title": "Senior Python Developer",
  "salary": "120000.00",
  "company_name": "ACME Corporation",
  "status": "open",
  "description": "Looking for an experienced Python developer...",
  "years_of_experience": 5,
  "created_by": {
    "id": 2,
    "username": "acme_admin",
    "email": "admin@acme.com",
    "is_company_admin": true,
    "company_name": "ACME Corporation"
  },
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z",
  "application_count": 0,
  "has_applied": false
}
```

---

### Step 6: Create Another Job
```bash
curl -X POST http://localhost:8000/api/jobs/ \
  -H "Authorization: Bearer <admin_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Junior Web Developer",
    "salary": "60000.00",
    "company_name": "ACME Corporation",
    "status": "open",
    "description": "Looking for a junior web developer with 1-2 years of experience.",
    "years_of_experience": 1
  }'
```

---

### Step 7: List All Open Jobs (Regular User)
```bash
curl -X GET http://localhost:8000/api/jobs/ \
  -H "Authorization: Bearer <user_token>"
```

**Expected Response (200):**
```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Senior Python Developer",
      "salary": "120000.00",
      "company_name": "ACME Corporation",
      "status": "open",
      "description": "...",
      "years_of_experience": 5,
      "created_by": {...},
      "created_at": "...",
      "updated_at": "...",
      "application_count": 0,
      "has_applied": false
    },
    {
      "id": 2,
      "title": "Junior Web Developer",
      "salary": "60000.00",
      "company_name": "ACME Corporation",
      "status": "open",
      "description": "...",
      "years_of_experience": 1,
      "created_by": {...},
      "created_at": "...",
      "updated_at": "...",
      "application_count": 0,
      "has_applied": false
    }
  ]
}
```

---

### Step 8: Get Job Details
```bash
curl -X GET http://localhost:8000/api/jobs/1/ \
  -H "Authorization: Bearer <user_token>"
```

---

### Step 9: Search Jobs by Title
```bash
curl -X GET "http://localhost:8000/api/jobs/search/?title=python" \
  -H "Authorization: Bearer <user_token>"
```

---

### Step 10: Search Jobs by Experience
```bash
curl -X GET "http://localhost:8000/api/jobs/search/?experience=5" \
  -H "Authorization: Bearer <user_token>"
```

---

### Step 11: Search Jobs by Title and Experience
```bash
curl -X GET "http://localhost:8000/api/jobs/search/?title=python&experience=5" \
  -H "Authorization: Bearer <user_token>"
```

---

### Step 12: Apply for a Job (Regular User)
```bash
curl -X POST http://localhost:8000/api/applications/ \
  -H "Authorization: Bearer <user_token>" \
  -H "Content-Type: application/json" \
  -d '{"job": 1}'
```

**Expected Response (201):**
```json
{
  "id": 1,
  "job": {
    "id": 1,
    "title": "Senior Python Developer",
    "salary": "120000.00",
    "company_name": "ACME Corporation",
    "status": "open",
    "description": "...",
    "years_of_experience": 5,
    "created_by": {...},
    "created_at": "...",
    "updated_at": "...",
    "application_count": 1,
    "has_applied": true
  },
  "applied_at": "2024-01-15T15:45:00Z"
}
```

---

### Step 13: Apply for Another Job
```bash
curl -X POST http://localhost:8000/api/applications/ \
  -H "Authorization: Bearer <user_token>" \
  -H "Content-Type: application/json" \
  -d '{"job": 2}'
```

---

### Step 14: View My Applications
```bash
curl -X GET http://localhost:8000/api/applications/ \
  -H "Authorization: Bearer <user_token>"
```

**Expected Response (200):**
```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 2,
      "job": {...},
      "applied_at": "..."
    },
    {
      "id": 1,
      "job": {...},
      "applied_at": "..."
    }
  ]
}
```

---

### Step 15: Try to Duplicate Application (Should Fail)
```bash
curl -X POST http://localhost:8000/api/applications/ \
  -H "Authorization: Bearer <user_token>" \
  -H "Content-Type: application/json" \
  -d '{"job": 1}'
```

**Expected Response (400):**
```json
{
  "error": "You have already applied for this job"
}
```

---

### Step 16: Update a Job (Admin Owner Only)
```bash
curl -X PUT http://localhost:8000/api/jobs/1/ \
  -H "Authorization: Bearer <admin_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Senior Python Developer (Updated)",
    "salary": "130000.00",
    "company_name": "ACME Corporation",
    "status": "open",
    "description": "Updated job description...",
    "years_of_experience": 5
  }'
```

---

### Step 17: Close a Job
```bash
curl -X PUT http://localhost:8000/api/jobs/1/ \
  -H "Authorization: Bearer <admin_token>" \
  -H "Content-Type: application/json" \
  -d '{"status": "closed"}'
```

---

### Step 18: Try to Apply to Closed Job (Should Fail)
```bash
curl -X POST http://localhost:8000/api/applications/ \
  -H "Authorization: Bearer <user_token>" \
  -H "Content-Type: application/json" \
  -d '{"job": 1}'
```

**Expected Response (400):**
```json
{
  "error": "Cannot apply to closed jobs"
}
```

---

### Step 19: Get Admin's Jobs
```bash
curl -X GET http://localhost:8000/api/jobs/admin_jobs/ \
  -H "Authorization: Bearer <admin_token>"
```

---

### Step 20: Delete a Job (Admin Owner Only)
```bash
curl -X DELETE http://localhost:8000/api/jobs/1/ \
  -H "Authorization: Bearer <admin_token>"
```

**Expected Response (204):** No content

---

## ERROR CASES TO TEST

### Test 1: Login with Wrong Password
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "wrongpassword"
  }'
```

**Expected Response (401):**
```json
{
  "detail": "Invalid credentials"
}
```

---

### Test 2: Register Company Admin Without Company Name
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "invalid_admin",
    "email": "invalid@example.com",
    "password": "securepassword123",
    "is_company_admin": true
  }'
```

**Expected Response (400):**
```json
{
  "company_name": [
    "Company name is required for company admins"
  ]
}
```

---

### Test 3: Regular User Try to Create Job
```bash
curl -X POST http://localhost:8000/api/jobs/ \
  -H "Authorization: Bearer <user_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test Job",
    "salary": "50000.00",
    "company_name": "Test Company",
    "status": "open",
    "description": "Test description",
    "years_of_experience": 0
  }'
```

**Expected Response (403):**
```json
{
  "detail": "Permission denied."
}
```

---

### Test 4: Update Someone Else's Job
```bash
# Create another admin account and try to update job created by first admin
curl -X PUT http://localhost:8000/api/jobs/1/ \
  -H "Authorization: Bearer <different_admin_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "closed"
  }'
```

**Expected Response (403):**
```json
{
  "detail": "Permission denied."
}
```

---

### Test 5: Access Without Token
```bash
curl -X GET http://localhost:8000/api/jobs/
```

**Expected Response (401):**
```json
{
  "detail": "Authentication credentials were not provided."
}
```

---

## ADMIN PANEL TESTING

1. Navigate to: http://localhost:8000/admin/
2. Login with superuser credentials (created with `python manage.py createsuperuser`)
3. Test:
   - View and manage users
   - Filter users by is_company_admin
   - View and manage jobs
   - View and manage applications
   - Search and filter functionality

---

## POSTMAN COLLECTION (Import into Postman)

Save this as a Postman collection (postman_collection.json):

```json
{
  "info": {
    "name": "Job Search API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Auth",
      "item": [
        {
          "name": "Register Regular User",
          "request": {
            "method": "POST",
            "url": "http://localhost:8000/api/register/",
            "body": {
              "raw": "{\"username\": \"john_doe\", \"email\": \"john@example.com\", \"password\": \"securepassword123\", \"is_company_admin\": false}"
            }
          }
        },
        {
          "name": "Register Company Admin",
          "request": {
            "method": "POST",
            "url": "http://localhost:8000/api/register/",
            "body": {
              "raw": "{\"username\": \"acme_admin\", \"email\": \"admin@acme.com\", \"password\": \"securepassword123\", \"is_company_admin\": true, \"company_name\": \"ACME Corporation\"}"
            }
          }
        },
        {
          "name": "Login",
          "request": {
            "method": "POST",
            "url": "http://localhost:8000/api/login/",
            "body": {
              "raw": "{\"username\": \"john_doe\", \"password\": \"securepassword123\"}"
            }
          }
        }
      ]
    },
    {
      "name": "Jobs",
      "item": [
        {
          "name": "List Jobs",
          "request": {
            "method": "GET",
            "url": "http://localhost:8000/api/jobs/",
            "header": {
              "key": "Authorization",
              "value": "Bearer <access_token>"
            }
          }
        },
        {
          "name": "Create Job",
          "request": {
            "method": "POST",
            "url": "http://localhost:8000/api/jobs/",
            "header": {
              "key": "Authorization",
              "value": "Bearer <admin_token>"
            },
            "body": {
              "raw": "{\"title\": \"Senior Python Developer\", \"salary\": \"120000.00\", \"company_name\": \"ACME Corporation\", \"status\": \"open\", \"description\": \"Looking for an experienced Python developer...\", \"years_of_experience\": 5}"
            }
          }
        }
      ]
    }
  ]
}
```

---

## PERFORMANCE TESTING

### Test Pagination
```bash
curl -X GET "http://localhost:8000/api/jobs/?page=1" \
  -H "Authorization: Bearer <user_token>"
```

### Test Large Number of Jobs
Create 100+ jobs and test pagination

---

## NOTES

- Replace `<user_token>` with the actual access token from a regular user login
- Replace `<admin_token>` with the actual access token from a company admin login
- All POST/PUT requests need `Content-Type: application/json` header
- Access tokens are valid for 60 minutes
- Each endpoint is protected and requires authentication (except register)
- Admin endpoints have additional permission checks

---

**Happy Testing! 🚀**
