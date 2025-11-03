# 📝 Task Manager — Django REST Framework + React (Vite)

> A modern full-stack Task Management web app built using **Django REST Framework (Backend)** and **React with Vite (Frontend)**.  
> Supports creating, viewing, updating, and deleting tasks with beautiful UI and toast notifications.

---

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Django](https://img.shields.io/badge/Django-REST%20Framework-092E20?logo=django)
![React](https://img.shields.io/badge/React-Vite-61DAFB?logo=react)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Features

- ✅ Add, View, Update, and Delete Tasks  
- 🧾 Each task includes `title`, `description`, `completed`, and `created_at` fields  
- 🧠 REST API powered by **Django REST Framework**  
- 💻 Responsive & clean UI built with **React + Vite + Bootstrap 5**  
- 🔔 Toast notifications for all user actions  
- ⚙️ Real-time status updates (completed / not completed)  
- 🌐 CORS enabled for smooth API communication  

---

## 🏗️ Project Structure

DRF/
├── backend/
│ ├── manage.py
│ ├── db.sqlite3
│ └── taskapp/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── admin.py
└── frontend/
├── package.json
├── vite.config.js
└── src/
├── App.jsx
├── main.jsx
└── index.css


---

## ⚙️ Backend Setup — Django REST API

```bash
# 1️⃣ Go to backend folder
cd backend

# 2️⃣ Create virtual environment
python -m venv env
env\Scripts\activate  # Windows

# 3️⃣ Install dependencies
pip install django djangorestframework django-cors-headers

# 4️⃣ Create migrations and run server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# API Based Url
http://127.0.0.1:8000/tasks/


# 1️⃣ Go to frontend folder
cd frontend

# 2️⃣ Install all packages
npm install

# 3️⃣ Install required libraries
npm install bootstrap react-bootstrap react-toastify

# 4️⃣ Start React app
npm run dev

http://localhost:5173

🪄 Features

✅ Add, Edit, Delete Tasks

✅ Mark tasks as Completed

✅ Toast notifications (success/error)

✅ Responsive UI (Mobile + Desktop)

✅ Live updates after CRUD actions

💡 How It Works

Django REST API handles all CRUD operations for tasks.

React frontend consumes the API using Axios.

Toast messages appear on each success or failure event.

State updates instantly without page reload.


| Method | Endpoint          | Description        |
| ------ | ----------------- | ------------------ |
| GET    | `/tasks/`     | Get all tasks      |
| POST   | `/tasks/`     | Create new task    |
| GET    | `/tasks/:id/` | Retrieve a task    |
| PATCH  | `/tasks/:id/` | Update task status |
| DELETE | `/tasks/:id/` | Delete task        |


🧑‍💻 Developer

👨‍💻 Pravin Patil
💼 Backend Developer (Python | Django | DRF | PostgreSQL | WebSockets)
🔗 GitHub Profile

🔗 LinkedIn Profile

