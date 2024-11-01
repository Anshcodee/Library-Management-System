# Library-Management-System

A web-based library management system built with Flask that helps librarians and students manage book borrowing efficiently.

Features

Multi-User System

Admin (Librarian) dashboard

Student portal



Admin Features

Manage book inventory

Track student borrowings

Handle borrow requests

View all registered students

Monitor book return status



Student Features

Browse available books

Request to borrow books

View borrowed books

Return books

Technology Stack

Backend: Python Flask

Database: SQLAlchemy, SQLite

Frontend: HTML, CSS, Jinja2 Templates



Project Structure
library_management_system/

│

├── static/

│   └── style.css

│

├── templates/

│   ├── base.html

│   ├── admin_base.html

│   ├── admin_inventory.html

│   ├── admin_students.html

│   ├── admin_requests.html

│   ├── login.html

│   ├── register.html

│   └── student_dashboard.html

│

├── models/

│   └── models.py

│

├── config.py

├── initialise_db.py

└── app.py


Installation

Clone the repository

git clone [https://github.com/yourusername/library-management-system.git](https://github.com/Anshcodee/Library-Management-System)


Create a virtual environment

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

(OR on mac:

virtualenv env

source env/bin/activate)


Install dependencies

pip install virtualenv

pip install flask

pip install flask flask-sqlalchemy


Set up the database

Run the initialise_db.py file

Run the application

python app.py


Usage

Access the application at http://localhost:5000

Register as a student or login as admin


Admin credentials:

Username: admin

Password: admin123
