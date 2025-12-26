# Hospital Management System - Authentication & API Setup Guide

## Installation

Install the required packages:
```bash
pip install -r requirements.txt
```

## Features Added

### 1. Authentication System
- User Registration (`/register/`)
- User Login (`/login/`)
- User Logout (`/logout/`)
- Session-based authentication
- @login_required decorators on protected views

### 2. CORS Middleware
- Enabled for localhost development
- Allows requests from http://localhost:3000, http://localhost:8000
- Configurable in settings.py

### 3. REST API Endpoints

#### Authentication
- POST `/api-auth/login/` - Login and get session
- POST `/api-auth/logout/` - Logout

#### Patient API (All require authentication)
- GET `/api/patients/` - List all patients
- POST `/api/patients/create/` - Create new patient
- GET `/api/patients/{id}/` - Get patient detail
- PUT `/api/patients/{id}/` - Update patient
- DELETE `/api/patients/{id}/` - Delete patient

#### Using the ViewSet
- GET `/api/patients/` - List all patients
- POST `/api/patients/` - Create new patient
- GET `/api/patients/{id}/` - Get patient detail
- PUT `/api/patients/{id}/` - Update patient
- PATCH `/api/patients/{id}/` - Partial update
- DELETE `/api/patients/{id}/` - Delete patient

## Database Migrations

If you modified the model, run:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Testing the API

### Using cURL:
```bash
# Login
curl -X POST http://localhost:8000/api-auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"user","password":"pass"}'

# Get patients
curl -X GET http://localhost:8000/api/patients/ \
  -H "Authorization: Bearer YOUR_TOKEN"

# Create patient
curl -X POST http://localhost:8000/api/patients/create/ \
  -H "Content-Type: application/json" \
  -d '{"name":"John","age":20,"gender":"","contact":"","medical_record_number":"MRN-001"}'
```

### Using Python:
```python
import requests

# Login
session = requests.Session()
response = session.post('http://localhost:8000/api-auth/login/', 
    data={'username': 'user', 'password': 'pass'})

# Get patients
response = session.get('http://localhost:8000/api/patients/')
print(response.json())

# Create patient
response = session.post('http://localhost:8000/api/patients/create/',
  json={'name': 'John', 'age': 20, 'gender': '', 'contact': '', 'medical_record_number': 'MRN-001'})
print(response.json())
```

# Web Interface URLs

- `/` - Home page (public)
- `/register/` - Register new account (public)
- `/login/` - Login page (public)
- `/logout/` - Logout (requires login)
- `/dashboard/` - Dashboard (requires login)
- `/add-patient/` - Add patient form (requires login)
- `/view-patients/` - View all patients (requires login)
- `/delete-patient/<id>/` - Delete patient (requires login)

## Configuration

### CORS Settings (settings.py)
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```

### REST Framework Settings
- Default authentication: SessionAuthentication
- Default permission: IsAuthenticated
- Pagination: 10 items per page
