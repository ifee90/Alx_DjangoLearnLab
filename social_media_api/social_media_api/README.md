# Social Media API

A Django REST Framework–based API that supports user registration and authentication using token-based login.

---

## 🚀 Features
- User registration (POST `/api/register/`)
- User login with token authentication (POST `/api/login/`)
- Django REST Framework setup and configuration
- Secure password storage and validation

---

## 🛠️ Technologies Used
- Python 3
- Django 4.2
- Django REST Framework (DRF)

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-link>
   cd social_media_api


2. **Run database migrations**
   ```bash
   python3 manage.py migrate


3. **Start the development server**
   ```bash
   python3 manage.py runserver


---

## 🔑 API Endpoints

### 1. Register User
**POST** `/api/register/`

**Request Body**
```json
{
  "username": "ifeoma",
  "email": "ifeoma@example.com",
  "password": "testpassword123"
}

{
  "message": "User registered successfully"
}


---

### 2. Login User
**POST** `/api/login/`

**Request Body**
```json
{
  "username": "ifeoma",
  "password": "testpassword123"
}

{
  "message": "Login successful",
  "token": "xxxxxxxxxxxxxxxxxxxx"
}


---

## 📄 License
This project is open-source and free to use for educational purposes.
