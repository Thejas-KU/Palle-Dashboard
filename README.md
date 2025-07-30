# Palle-Dashboard
🌾 Palle Dashboard – Role-Based Institution Management System
Palle Dashboard is a Role-Based Access Control (RBAC) web application built with Django to efficiently manage employees and students in an educational institution or training center. It features dynamic dashboards based on user roles (Admin & Sales) with secure authentication and data integrity.

🚀 Features at a Glance
👑 Admin Role (Full Access)
🧑‍💼 Manage Employees – Add, View, Delete

🎓 Manage Students – Add, View, Edit, Delete

🔄 Assign students to any employee via added_by dropdown

📊 Full Admin Dashboard with all data & actions

📋 Sales Role (Restricted Access)
➕ Add Students (auto-assigns added_by to logged-in Sales user)

👀 View Student List (Read-Only)

🚫 Cannot modify/delete students or view employees

🔐 Authentication & Workflow
Superuser Creation – via python manage.py createsuperuser

Role-Based Redirects – Admin → Admin Dashboard | Sales → Sales Dashboard

Personalized Welcome Message – "Welcome, [Username]"

Secure Session Handling – CSRF protection, proper login/logout

🛠 Tech Stack
Layer	Technology
Backend	Python, Django (FBVs, ORM, Authentication)
Frontend	HTML, Bootstrap, CSS, Django Templates
Database	MySQL (Normalized Schema)
Security	Role-Based Access, CSRF Protection, Session Management

📂 System Architecture
Admin Dashboard
Navbar: Employee List | Student List | Logout

CRUD Operations on Employees & Students

Student Creation with full added_by control

Sales Dashboard
Navbar: Add Student | View Students | Logout

Add Student (auto-filled added_by)

View Students (read-only)

⚡ Technical Highlights
Django ORM for .filter(), .get(), .create(), .update() operations

Function-Based Views (FBVs) for better control and readability

ModelForms for clean form validation & data handling

Django Admin Panel extended with filters & inline edits

Message Framework for success/error notifications

🔒 Security & Data Integrity
✅ Role-based feature restrictions
✅ Controlled added_by field (tamper-proof)
✅ CSRF protection for all POST requests
✅ Proper session management & redirects

📦 Installation & Setup
bash
Copy
Edit
# 1️⃣ Clone the repository
git clone https://github.com/your-username/palle-dashboard.git
cd palle-dashboard

# 2️⃣ Create & activate virtual environment
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Configure database in settings.py (MySQL)
# Update NAME, USER, PASSWORD, HOST, PORT

# 5️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

# 6️⃣ Create superuser
python manage.py createsuperuser

# 7️⃣ Run the server
python manage.py runserver
📝 Summary
Admins → Full CRUD access on employees & students

Sales → Add & view students (read-only)

Dynamic Dashboards → Role-based redirects and navbar options

Clean & Secure → ORM, FBVs, CSRF, Session handling

Scalable → Can easily extend roles & permissions

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License
This project is licensed under the MIT License – feel free to use and modify.
