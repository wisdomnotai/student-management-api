
# Student Management API – FastAPI CRUD for Student Records

A lightweight, developer-friendly API for managing student records, built with **FastAPI** and **Pydantic**. Created by Wisdom Alawode, a math student at the University of Ibadan, Oyo State, Nigeria.

This API lets you create, read, update, and delete student data without the hassle of a full database setup — perfect for learning backend development, quick prototypes, and testing REST clients.


## Mission

Make learning API development easier by providing a simple, fully functional CRUD backend that anyone can run locally in minutes.


## Project Overview

### 🎯 Goals

* **CRUD Learning Tool** – Teach beginners how Create, Read, Update, and Delete works in an API.
* **Lightweight Backend** – No external database; runs fully in memory.
* **Beginner-Friendly Code** – Clean, well-commented Python code for easy understanding.

### 📲 Key Features Implemented

✅ Create new student records via POST requests
✅ Retrieve student details by ID or name
✅ Update student records with partial or full updates
✅ Delete students by ID
✅ List all students with total count


## 📘 What the API Does

* **Create Students** – Add new students with name, age, and year.
* **Read Students** – Get a student by ID, search by name, or list all students.
* **Update Students** – Modify one or more fields for an existing student.
* **Delete Students** – Remove a student from the database.

## Who It’s For

* **Python beginners** learning APIs
* Developers testing frontends with a live backend
* Students building practice projects in FastAPI

## 🛠 Built With

* **Language:** Python
* **Framework:** FastAPI
* **Validation:** Pydantic
* **Server:** Uvicorn


## 🧩 How It Works

1. Run the API locally with Uvicorn.
2. Use tools like **cURL**, **Postman**, or your frontend to send HTTP requests.
3. The API processes requests in-memory (no database).
4. Data resets each time the server restarts — perfect for testing.

---

## 🚀 Installation & Usage

```bash
# 1️⃣ Clone the repository
git clone https://github.com/wisdomnotai/student-management-api.git

# 2️⃣ Navigate into the project
cd student-management-api

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the API
uvicorn app:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

## Want to Contribute?

This project is open source — contributions are welcome!

Whether you want to:

* Add database support
* Improve validation
* Expand API endpoints
* Add authentication

👉 Fork it, clone it, and submit a PR!

