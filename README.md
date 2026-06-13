# 📝 Flask To-Do List App

A simple yet functional To-Do List application built with Flask, SQLAlchemy, and custom CSS. Manage your tasks efficiently with status tracking and user authentication.

![Flask](https://img.shields.io/badge/Flask-2.3.3-black)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![SQLite](https://img.shields.io/badge/SQLite-3-green)
![License](https://img.shields.io/badge/License-MIT-red)

## ✨ Features

- 🔐 **User Authentication** - Login/Logout system
- ✅ **Task Management** - Create, read, update, and delete tasks
- 🔄 **Status Tracking** - Cycle through: Pending → Working → Done
- 🗑️ **Bulk Operations** - Clear all tasks at once
- 💬 **Flash Messages** - Instant feedback for user actions
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- 🎨 **Modern UI** - Clean and intuitive interface

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Flask | Web framework |
| SQLAlchemy | ORM (Object Relational Mapper) |
| SQLite | Database |
| HTML5 | Structure |
| CSS3 | Styling |
| JavaScript | Frontend interactivity |

## 📁 Project Structure
flask-todo-app/
├── app/
│ ├── init.py # App factory
│ ├── models.py # Database models
│ ├── routes/
│ │ ├── init.py
│ │ ├── auth.py # Authentication routes
│ │ └── tasks.py # Task management routes
│ ├── static/
│ │ ├── css/
│ │ │ └── style.css # Styling
│ │ └── js/
│ │ └── script.js # JavaScript
│ └── templates/
│ ├── base.html # Base template
│ ├── login.html # Login page
│ ├── register.html # Registration page
│ └── tasks.html # Tasks dashboard
├── instance/
│ └── todo.db # SQLite database (auto-generated)
├── run.py # Application entry point
├── requirements.txt # Dependencies
└── README.md # Documentation


## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/flask-todo-app.git
   cd flask-todo-app

## Create a virtual environment
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

### Install dependencies
-pip install -r requirements.txt

### Run the application
-python3 run.py

### Open your browser
-http://127.0.0.1:5000



🔑 Login Credentials
Username	Password
admin	1234
Note: Change the default credentials in app/routes/auth.py for production use.

📖 Usage Guide
1. Login
Enter username: admin

Enter password: 1234

Click "Login"

2. Managing Tasks
Action	How to do it
Add task	Type task name → Click "Add Task"
Update status	Click "Next Status" button
Delete single task	Click "Delete" button
Clear all tasks	Click "Clear All Tasks"
Logout	Click "Logout" in navigation
3. Status Flow
text
Pending → Working → Done → Pending
📡 API Endpoints
Method	Endpoint	Description	Auth Required
GET, POST	/auth/login	User login	No
GET	/auth/logout	User logout	Yes
GET	/	View all tasks	Yes
POST	/add	Add new task	Yes
POST	/toggle/<id>	Update task status	Yes
POST	/clear	Delete all tasks	Yes
POST	/delete/<id>	Delete single task	Yes
🎯 Features in Detail
Task Status Management
Pending (Yellow) - Task not started

Working (Blue) - Task in progress

Done (Green) - Task completed

Flash Messages
Green: Success (login, add task, delete)

Red: Error/Alert (clear all tasks)

Blue: Info (status update)

Yellow: Warning (invalid login)

🔧 Customization
Change Default Credentials
Edit app/routes/auth.py:

python
USER_CREDENTIALS = {
    "your_username": "your_password"
}
Change Secret Key
Edit app/__init__.py:

python
app.config['SECRET_KEY'] = 'your-secure-key-here'
Use Different Database
Edit app/__init__.py:

python
# PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/dbname'

# MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:pass@localhost/dbname'
🐛 Troubleshooting
Issue	Solution
Module not found	Run pip install -r requirements.txt
Database error	Delete instance/todo.db and restart
Port already in use	Change port: app.run(debug=True, port=5001)
Login doesn't work	Check credentials in auth.py
📦 Deployment
Deploy to Render (Free)
Push code to GitHub

Create render.yaml:

yaml
services:
  - type: web
    name: flask-todo
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn run:app
Deploy to PythonAnywhere
Upload files to PythonAnywhere

Set up virtual environment

Configure WSGI file

🤝 Contributing
Contributions are welcome! Here's how:

Fork the repository

Create feature branch (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
Distributed under the MIT License. See LICENSE file for more information.

👨‍💻 Author
Gungun

GitHub: GungunSinghal03

🙏 Acknowledgments
Flask Documentation

SQLAlchemy ORM

Bootstrap (design inspiration)

📧 Contact
For questions or feedback, please open an issue on GitHub.



