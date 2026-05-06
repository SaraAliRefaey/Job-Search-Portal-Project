# ⚡ QUICK REFERENCE - Job Search Backend

## 🚀 GET STARTED IN 3 STEPS

```bash
# 1. Activate environment
cd myproject && venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run server
python manage.py runserver
```

**API is live at:** http://localhost:8000/api/

---

## 📋 QUICK COMMANDS

| Command | Purpose |
|---------|---------|
| `python manage.py runserver` | Start dev server |
| `python manage.py migrate` | Apply migrations |
| `python manage.py createsuperuser` | Create admin user |
| `python manage.py check --deploy` | Check settings |
| `python EXAMPLE_USAGE.py` | Run test examples |

---

## 🔑 API ENDPOINTS

### Auth
```
POST /api/register/    - Register user
POST /api/login/       - Login & get token
```

### Jobs
```
GET  /api/jobs/                - List jobs
POST /api/jobs/                - Create job (admin)
GET  /api/jobs/search/         - Search jobs
GET  /api/jobs/admin_jobs/     - My jobs (admin)
GET  /api/jobs/{id}/           - Job details
PUT  /api/jobs/{id}/           - Update job (owner)
DEL  /api/jobs/{id}/           - Delete job (owner)
```

### Applications
```
POST /api/applications/        - Apply for job
GET  /api/applications/        - My applications
```

---

## 📝 QUICK EXAMPLES

### Register
```json
POST /api/register/
{
  "username": "john",
  "email": "john@example.com",
  "password": "secure123",
  "is_company_admin": false
}
```

### Login
```json
POST /api/login/
{
  "username": "john",
  "password": "secure123"
}
→ Response: { "access": "token...", "refresh": "token..." }
```

### List Jobs
```
GET /api/jobs/
Authorization: Bearer <token>
```

### Search Jobs
```
GET /api/jobs/search/?title=python&experience=5
Authorization: Bearer <token>
```

### Apply for Job
```json
POST /api/applications/
Authorization: Bearer <token>
{
  "job": 1
}
```

---

## 🔐 USER ROLES

### Company Admin
- ✅ Create jobs
- ✅ Update own jobs
- ✅ Delete own jobs
- ✅ View all jobs

### Regular User
- ✅ View open jobs
- ✅ Search jobs
- ✅ Apply for jobs
- ✅ View applications

---

## 🗂️ KEY FILES

| File | Purpose |
|------|---------|
| `models.py` | Database models (3 models) |
| `serializers.py` | API serializers (6 serializers) |
| `views.py` | API endpoints (4 viewsets) |
| `permissions.py` | Access control (3 permissions) |
| `urls.py` | API routes |
| `admin.py` | Admin panel |

---

## 💻 CURL EXAMPLES

### Register
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"john","email":"john@test.com","password":"pass123","is_company_admin":false}'
```

### Login
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"john","password":"pass123"}'
```

### List Jobs
```bash
curl http://localhost:8000/api/jobs/ \
  -H "Authorization: Bearer TOKEN"
```

### Create Job (Admin)
```bash
curl -X POST http://localhost:8000/api/jobs/ \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title":"Python Dev",
    "salary":"100000",
    "company_name":"ACME",
    "description":"Senior role",
    "years_of_experience":5
  }'
```

### Search
```bash
curl "http://localhost:8000/api/jobs/search/?title=python" \
  -H "Authorization: Bearer TOKEN"
```

### Apply
```bash
curl -X POST http://localhost:8000/api/applications/ \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"job":1}'
```

---

## 🗄️ DATABASE MODELS

### CustomUser
```
- username (unique)
- email (unique)
- password (hashed)
- is_company_admin (boolean)
- company_name (string, optional)
```

### Job
```
- title
- salary
- company_name
- status (open/closed)
- description
- years_of_experience
- created_by (FK → User)
- created_at (auto)
- updated_at (auto)
```

### JobApplication
```
- user (FK)
- job (FK)
- applied_at (auto)
- Constraint: unique(user, job)
```

---

## ✅ VALIDATION RULES

✅ Company name required if is_company_admin=true
✅ No duplicate applications to same job
✅ Can only apply to open jobs
✅ Only admin can create jobs
✅ Only job creator can update/delete job
✅ Years of experience must be >= 0
✅ Status must be 'open' or 'closed'

---

## 🔒 SECURITY

- ✅ JWT token authentication
- ✅ Password hashing (PBKDF2)
- ✅ Permission-based access
- ✅ CSRF protection
- ✅ Input validation
- ✅ SQL injection prevention

---

## 📚 DOCUMENTATION FILES

| File | Size | Content |
|------|------|---------|
| README.md | Large | Complete guide |
| IMPLEMENTATION_SUMMARY.md | Large | Technical details |
| API_TEST_COMMANDS.md | Medium | Test workflow |
| EXAMPLE_USAGE.py | Medium | Python examples |
| FINAL_SUMMARY.md | Large | Project overview |
| requirements.txt | Small | Dependencies |

---

## 🧪 TEST WORKFLOW

1. **Register user:**
   ```bash
   POST /api/register/
   ```

2. **Login:**
   ```bash
   POST /api/login/ → Get token
   ```

3. **Create job (admin):**
   ```bash
   POST /api/jobs/
   ```

4. **List jobs:**
   ```bash
   GET /api/jobs/
   ```

5. **Search:**
   ```bash
   GET /api/jobs/search/?title=...
   ```

6. **Apply:**
   ```bash
   POST /api/applications/
   ```

7. **My applications:**
   ```bash
   GET /api/applications/
   ```

---

## 🛠️ TROUBLESHOOTING

| Issue | Solution |
|-------|----------|
| Django not found | Run: `pip install -r requirements.txt` |
| Database error | Run: `python manage.py migrate` |
| Port in use | Run: `python manage.py runserver 8001` |
| Permission denied | Check user role (is_company_admin) |
| Token invalid | Login again to get new token |
| 404 on endpoint | Check URL in browser first |

---

## 🚀 DEPLOYMENT

### Before deploying:
- [ ] Set DEBUG = False
- [ ] Change SECRET_KEY
- [ ] Set ALLOWED_HOSTS
- [ ] Use PostgreSQL
- [ ] Setup HTTPS
- [ ] Configure environment variables

### Deploy with:
- Gunicorn (WSGI server)
- Nginx (reverse proxy)
- PostgreSQL (database)
- Let's Encrypt (SSL)

---

## 📞 SUPPORT

- **Setup issues?** → Check README.md
- **Testing?** → See API_TEST_COMMANDS.md
- **Code examples?** → Run EXAMPLE_USAGE.py
- **Technical details?** → Read IMPLEMENTATION_SUMMARY.md
- **Overview?** → See FINAL_SUMMARY.md

---

## 🎯 COMMON TASKS

### Create a job
```bash
# As company admin with token:
curl -X POST http://localhost:8000/api/jobs/ \
  -H "Authorization: Bearer ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{...job data...}'
```

### Search jobs
```bash
# As any authenticated user:
curl "http://localhost:8000/api/jobs/search/?title=python&experience=5" \
  -H "Authorization: Bearer USER_TOKEN"
```

### Apply for job
```bash
# As regular user:
curl -X POST http://localhost:8000/api/applications/ \
  -H "Authorization: Bearer USER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"job": 1}'
```

### View my applications
```bash
# As any authenticated user:
curl http://localhost:8000/api/applications/ \
  -H "Authorization: Bearer TOKEN"
```

---

## 📊 API RESPONSE CODES

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Created |
| 204 | Deleted |
| 400 | Bad request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not found |
| 500 | Server error |

---

## 🌐 URLs

- Main API: http://localhost:8000/api/
- Admin Panel: http://localhost:8000/admin/
- Browsable API: http://localhost:8000/api/jobs/

---

## 🎓 FILES TO READ FIRST

1. **FINAL_SUMMARY.md** ← Start here for overview
2. **README.md** ← For detailed documentation
3. **API_TEST_COMMANDS.md** ← For testing
4. **IMPLEMENTATION_SUMMARY.md** ← For technical details

---

## ✨ KEY FEATURES AT A GLANCE

✅ 2 User roles (Company Admin, Regular User)
✅ JWT authentication
✅ 12 API endpoints
✅ Full job management
✅ Job search & filtering
✅ Application tracking
✅ Admin panel
✅ Complete documentation
✅ 50+ code examples
✅ Production-ready code

---

## 🎉 YOU'RE ALL SET!

Your backend is ready to:
- ✅ Accept API requests
- ✅ Authenticate users
- ✅ Manage jobs
- ✅ Track applications
- ✅ Scale to production

**Start the server and begin using it now!**

---

```
python manage.py runserver
→ http://localhost:8000/api/
```

**Happy coding! 🚀**

---

*Version: 1.0*
*Django: 6.0.4*
*Status: ✅ Ready*
