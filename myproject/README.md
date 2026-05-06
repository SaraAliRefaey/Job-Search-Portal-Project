# Job Search Website Backend

A complete Django REST Framework backend for a job search website with JWT authentication, role-based access control, and comprehensive job management features.

## 📋 Project Description

This is a full-featured backend API for a job search platform that allows:
- **Company Admins**: Post and manage job listings
- **Regular Users**: Search for jobs and apply to positions

The project uses Django REST Framework for API development, Simple JWT for authentication, and SQLite for data persistence.

## ✨ Features

### Authentication & Authorization
- ✅ User registration (two roles: Company Admin, Regular User)
- ✅ JWT-based login with token refresh
- ✅ Password hashing and validation
- ✅ Role-based access control

### Job Management
- ✅ Create, update, delete job postings (Admin only)
- ✅ View all open jobs (Regular users)
- ✅ Search jobs by title and experience level
- ✅ Filter jobs by status (open/closed)
- ✅ Track job metadata (creation date, creator, application count)

### Job Applications
- ✅ Apply for open jobs
- ✅ Prevent duplicate applications
- ✅ Prevent applying to closed jobs
- ✅ View application history

### Additional Features
- ✅ Admin panel for database management
- ✅ Comprehensive API documentation via router
- ✅ Proper error handling and validation
- ✅ RESTful API design
- ✅ Pagination support

## 🛠️ Tech Stack

- **Django 6.0.4**: Web framework
- **Django REST Framework 3.17.1**: REST API development
- **djangorestframework-simplejwt 5.5.1**: JWT authentication
- **SQLite**: Database (default)
- **Python 3.13**: Programming language

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Setup

1. **Clone or navigate to the project**
   ```bash
   cd myproject
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin panel)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/api/`

## 🔧 Quick Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser for admin panel
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Run tests
python manage.py test

# Access admin panel
# Navigate to http://localhost:8000/admin/
```

## 📚 API Endpoints

### Authentication Endpoints

#### Register User
```
POST /api/register/
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123",
  "is_company_admin": false
}
```
**Response (201):**
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "is_company_admin": false,
  "company_name": null
}
```

#### Register Company Admin
```
POST /api/register/
Content-Type: application/json

{
  "username": "acme_admin",
  "email": "admin@acme.com",
  "password": "securepassword123",
  "is_company_admin": true,
  "company_name": "ACME Corporation"
}
```

#### Login
```
POST /api/login/
Content-Type: application/json

{
  "username": "john_doe",
  "password": "securepassword123"
}
```
**Response (200):**
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Job Endpoints

#### List All Open Jobs
```
GET /api/jobs/
Authorization: Bearer <access_token>
```
**Response (200):**
```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
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
      "application_count": 3,
      "has_applied": false
    }
  ]
}
```

#### Get Job Details
```
GET /api/jobs/{id}/
Authorization: Bearer <access_token>
```

#### Create Job (Admin Only)
```
POST /api/jobs/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "title": "Senior Python Developer",
  "salary": "120000.00",
  "company_name": "ACME Corporation",
  "status": "open",
  "description": "Looking for an experienced Python developer with 5+ years of experience...",
  "years_of_experience": 5
}
```
**Response (201):**
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

#### Update Job (Admin Owner Only)
```
PUT /api/jobs/{id}/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "title": "Senior Python Developer (Updated)",
  "salary": "130000.00",
  "company_name": "ACME Corporation",
  "status": "open",
  "description": "Updated description...",
  "years_of_experience": 5
}
```

#### Delete Job (Admin Owner Only)
```
DELETE /api/jobs/{id}/
Authorization: Bearer <access_token>
```

#### Search Jobs
```
GET /api/jobs/search/?title=python&experience=5
Authorization: Bearer <access_token>
```
**Query Parameters:**
- `title` (optional): Search by job title (partial match)
- `experience` (optional): Filter by years of experience (exact match)

#### Get Admin's Jobs
```
GET /api/jobs/admin_jobs/
Authorization: Bearer <access_token>
```
(Company Admin only - lists all jobs created by the admin)

### Job Application Endpoints

#### Apply for Job
```
POST /api/applications/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "job": 1
}
```
**Response (201):**
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
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z",
    "application_count": 4,
    "has_applied": true
  },
  "applied_at": "2024-01-15T15:45:00Z"
}
```

#### Get My Applications
```
GET /api/applications/
Authorization: Bearer <access_token>
```
or
```
GET /api/applications/my_applications/
Authorization: Bearer <access_token>
```

## 🔐 Authentication

This API uses **JWT (JSON Web Tokens)** for authentication.

### How to Use JWT:

1. **Register a new user:**
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

2. **Login to get tokens:**
   ```bash
   curl -X POST http://localhost:8000/api/login/ \
     -H "Content-Type: application/json" \
     -d '{
       "username": "john_doe",
       "password": "securepassword123"
     }'
   ```

3. **Use the access token in requests:**
   ```bash
   curl -X GET http://localhost:8000/api/jobs/ \
     -H "Authorization: Bearer <your_access_token>"
   ```

4. **Token Lifetime:**
   - Access Token: 60 minutes
   - Refresh Token: 1 day

## 🗂️ Project Structure

```
myproject/
├── myproject/                 # Main project settings
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL configuration
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
├── jobs/                      # Jobs app
│   ├── migrations/           # Database migrations
│   ├── admin.py              # Admin panel configuration
│   ├── apps.py               # App configuration
│   ├── models.py             # Database models
│   ├── serializers.py        # API serializers
│   ├── views.py              # API views
│   ├── permissions.py        # Custom permissions
│   ├── urls.py               # App URL configuration
│   └── tests.py              # Tests
├── students/                  # Example app (can be removed)
├── db.sqlite3                # SQLite database
├── manage.py                 # Django management script
└── requirements.txt          # Project dependencies
```

## 📊 Database Models

### CustomUser Model
```
- id (Primary Key)
- username (Unique)
- email (Unique)
- password (Hashed)
- is_company_admin (Boolean)
- company_name (String, optional)
- is_active (Boolean)
- is_staff (Boolean)
- date_joined (DateTime)
```

### Job Model
```
- id (Primary Key)
- title (String)
- salary (Decimal)
- company_name (String)
- status (Choices: 'open', 'closed')
- description (Text)
- years_of_experience (Integer)
- created_by (ForeignKey → CustomUser)
- created_at (DateTime)
- updated_at (DateTime)
```

### JobApplication Model
```
- id (Primary Key)
- user (ForeignKey → CustomUser)
- job (ForeignKey → Job)
- applied_at (DateTime)
- Unique Constraint: (user, job)
```

## 🔒 Permissions & Access Control

### Company Admin Permissions:
- ✅ Create new job postings
- ✅ Update their own job postings
- ✅ Delete their own job postings
- ✅ View all jobs (open and closed)
- ✅ View their own created jobs
- ✅ Cannot apply for jobs

### Regular User Permissions:
- ✅ View all open jobs
- ✅ Search for jobs
- ✅ Apply for open jobs
- ✅ View their application history
- ✅ Cannot create/update/delete jobs

## 🧪 Example Usage with Python Requests

```python
import requests

BASE_URL = "http://localhost:8000/api"

# Register as regular user
register_data = {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "is_company_admin": False
}
response = requests.post(f"{BASE_URL}/register/", json=register_data)
print(response.json())

# Login
login_data = {
    "username": "john_doe",
    "password": "securepassword123"
}
response = requests.post(f"{BASE_URL}/login/", json=login_data)
tokens = response.json()
access_token = tokens["access"]

# Get all jobs
headers = {"Authorization": f"Bearer {access_token}"}
response = requests.get(f"{BASE_URL}/jobs/", headers=headers)
print(response.json())

# Search jobs
response = requests.get(f"{BASE_URL}/jobs/search/", params={
    "title": "python",
    "experience": 5
}, headers=headers)
print(response.json())

# Apply for a job
apply_data = {"job": 1}
response = requests.post(f"{BASE_URL}/applications/", json=apply_data, headers=headers)
print(response.json())

# Get my applications
response = requests.get(f"{BASE_URL}/applications/", headers=headers)
print(response.json())
```

## 📝 Example Usage with cURL

```bash
# Register
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "is_company_admin": false
  }'

# Login
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "securepassword123"
  }'

# List jobs
curl -X GET http://localhost:8000/api/jobs/ \
  -H "Authorization: Bearer <access_token>"

# Search jobs
curl -X GET "http://localhost:8000/api/jobs/search/?title=python&experience=5" \
  -H "Authorization: Bearer <access_token>"

# Apply for job
curl -X POST http://localhost:8000/api/applications/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"job": 1}'
```

## 🎯 Key Features Implemented

### ✅ Authentication
- User registration with role selection
- JWT-based authentication
- Secure password hashing

### ✅ Job Management
- Full CRUD operations for jobs
- Job status management (open/closed)
- Company-specific job listings
- Automatic timestamps

### ✅ Job Search & Filtering
- Search by job title
- Filter by years of experience
- Open job filtering for regular users

### ✅ Application System
- Apply for jobs
- Prevent duplicate applications
- Prevent applying to closed jobs
- Track application history

### ✅ Permission System
- Role-based access control
- Admin-only endpoints
- Owner-only update/delete
- Proper error responses

### ✅ Admin Panel
- Manage users, jobs, and applications
- Filter and search capabilities
- Admin-friendly interface

## 🚀 Deployment Notes

For production deployment:

1. **Security Updates:**
   ```python
   # In settings.py
   DEBUG = False
   ALLOWED_HOSTS = ['your-domain.com']
   SECRET_KEY = 'use-environment-variable'
   ```

2. **Database:**
   - Consider using PostgreSQL instead of SQLite
   - Set up proper backups

3. **Static Files:**
   ```bash
   python manage.py collectstatic
   ```

4. **Use production WSGI server:**
   - Gunicorn
   - uWSGI
   - etc.

5. **Enable HTTPS:**
   - Use SSL/TLS certificates
   - Configure CSRF settings

## 📖 API Documentation

The Django REST Framework automatically provides:
- Browsable API at each endpoint
- Interactive API documentation
- Action buttons for testing

Visit `http://localhost:8000/api/` to explore the API interactively.

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:
1. Create a feature branch
2. Make your changes
3. Write or update tests
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## ❓ FAQ

**Q: How do I create a company admin user?**
A: Use the registration endpoint with `"is_company_admin": true` and provide a `company_name`.

**Q: Can regular users see closed jobs?**
A: No, regular users only see open jobs. Company admins can see all jobs.

**Q: Can I apply to a job multiple times?**
A: No, the system prevents duplicate applications with a unique constraint.

**Q: How long are JWT tokens valid?**
A: Access tokens are valid for 60 minutes, refresh tokens for 1 day.

**Q: How do I access the admin panel?**
A: Navigate to `http://localhost:8000/admin/` and login with your superuser credentials.

## 📞 Support

For issues or questions:
1. Check the FAQ section
2. Review the API documentation
3. Check Django and DRF documentation
4. Open an issue in the repository

---

**Created with ❤️ using Django and Django REST Framework**

**Last Updated:** January 2024
**Django Version:** 6.0.4
**Python Version:** 3.13+
