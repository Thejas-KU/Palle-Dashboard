# 🧑‍💼  Palle Dashboard – Role-Based Institution Management System

A *role-based access control (RBAC)* system built using *Django* for managing employees and students efficiently. The project supports two user roles — *Admin* and *Sales* — with different levels of access and dynamic dashboards.

---

## 📌 Features

### 🔐 Role-Based Permissions

| Role  | Permissions |
|-------|-------------|
| *Admin (Superuser)* | ✅ Full CRUD on Employees & Students<br>✅ Access to Admin Dashboard<br>✅ Assign students to any employee |
| *Sales* | ✅ Add Students<br>👁 View-only access to Students<br>🚫 No access to Employees<br>🔒 Cannot edit/delete students |

---

## 🔄 System Workflow

### 👤 Authentication Flow
- *Superuser* created using Django's createsuperuser command.
- Upon login:
  - *Admins* are redirected to the *Admin Dashboard*.
  - *Sales* users are redirected to the *Sales Dashboard*.
- Displays welcome message: "Welcome, [username]".

### 🧭 Navigation

#### Admin Dashboard
- 🧑‍💼 Employee List (View/Add/Delete)
- 🎓 Student List (View/Edit/Delete)
- 🔒 Logout
- 🎓 Add Student (select added_by from dropdown)

#### Sales Dashboard
- ➕ Add Student (auto-filled added_by)
- 👁 View Students (Read-only)
- 🔒 Logout

---

## 🧱 Technical Highlights

- *Backend:* Python, Django (FBVs, ORM)
- *Frontend:* HTML, CSS, Bootstrap, Django Templates
- *Database:* MySQL (normalized schema)

### 🛠 Django Features Used
- ✅ Function-Based Views for custom logic
- ✅ Django ORM for database operations (.filter(), .get(), .create(), .update())
- ✅ ModelForm for form validation and input handling
- ✅ Django Admin Panel extended with filters and inline editing
- ✅ Session & Messaging Framework for success/error notifications
- ✅ CSRF protection enabled for all forms

---

## 🔒 Security & Data Integrity

- 🔐 Role-based access with conditional rendering
- 🔐 Auto-controlled added_by field to prevent tampering
- 🔐 Secure session handling with login/logout redirects
- 🔐 CSRF tokens enforced in all POST forms

---

## 📦 How to Run Locally

bash
# Clone the repository
git clone https://github.com/your-username/palle-admin-dashboard.git
cd palle-admin-dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Migrate the database
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run the server
python manage.py runserver
