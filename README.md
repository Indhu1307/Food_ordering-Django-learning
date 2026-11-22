# 🍔 Food Ordering System

A web-based **Food Ordering System** developed using Python and Django. This project allows users to explore food items, view food details, and manage their food ordering process.

## 🚀 Project Overview

The Food Ordering System is designed to make online food ordering simple and convenient. It provides an organized platform to manage food menus, user accounts, shopping cart functionality, and orders.

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS
- **Backend:** Python, Django
- **Database:** MySQL / SQLite (based on project configuration)
- **IDE:** Visual Studio Code
- **Version Control:** Git & GitHub

## 📂 Project Structure

```text
Food-ordering/
│
├── FoodOrdering/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── admin.py
│
├── cart/
│   ├── migrations/
│   ├── models.py
│   └── views.py
│
├── menu/
│   ├── migrations/
│   ├── templates/
│   │   └── menu/
│   │       └── food_list.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── orders/
│   ├── migrations/
│   ├── models.py
│   └── views.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## ✨ Main Modules

- **Accounts:** User account management.
- **Menu:** Display and manage food items.
- **Cart:** Manage selected food items.
- **Orders:** Handle customer orders.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Indhu1307/Food_ordering-Django-learning.git
```

### 2. Navigate to the project folder

```bash
cd Food_ordering-Django-learning
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate virtual environment

Windows:

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the Django server

```bash
python manage.py runserver
```

Open your browser and visit:

`http://127.0.0.1:8000/foods/`

## 🔐 Create Django Superuser

To access the Django Admin Panel, create a superuser account.

### 1. Run the following command

```bash
python manage.py createsuperuser
```

### 2. Enter admin details

```text
Username: admin
Email address: admin@example.com
Password: Enter your password
Password (again): Confirm your password
```

### 3. Start the development server

```bash
python manage.py runserver
```

### 4. Access Django Admin Panel

Open the following URL in your browser:

```text
http://127.0.0.1:8000/admin/
```

Login using your superuser username and password.

**Note:** Never share or upload your admin password to GitHub.

## 🎯 Project Objective

The main objective of this project is to develop a simple food ordering application using Django and understand real-world web application development concepts.

## 👩‍💻 Developer

**Indhu**

GitHub: [Indhu1307](https://github.com/Indhu1307)

---

⭐ If you find this project useful, feel free to explore the repository!
