🏥 Hospital Portal — Role-Based Django Web Application

A Django-based web application that provides role-based authentication for Doctors and Patients, along with a Blog Management System where doctors can create, edit, and delete blog posts, and patients can view & comment on them.

🚀 Features
👨‍⚕️ Doctor Portal

Login & Role-Based Dashboard

Create Blog Posts

Edit & Delete Blog Posts

Upload Blog Images

Set category (COVID, Immunization, First Aid, Nutrition, Mental Health, etc.)

Save blog as Draft or Published

🧑‍⚕️ Patient Portal

Login & Role-Based Dashboard

View All Published Blogs

Read full blog with image + summary

View blogs category-wise

Comment on blog posts

🔐 Authentication System

Custom User Model with role field:

doctor

patient

Secure login/logout

Role-based restriction middleware

Redirects based on user role

📁 Project Structure
hospital_portal/
│── blog/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/blog/
│
│── core/
│   ├── models.py  (Custom User Model)
│   ├── views.py   (Login/Signup)
│   ├── urls.py
│   └── templates/core/
│
│── templates/
│   ├── base.html
│   ├── doctor_dashboard.html
│   └── patient_dashboard.html
│
│── media/  (Uploaded images)
│
└── settings.py

🛠 Setup Instructions
1️⃣ Clone the project
git clone <repo-url>
cd hospital_portal

2️⃣ Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure MySQL
Create database:
CREATE DATABASE hospital_portal;

Add DB credentials in settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hospital_portal',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5️⃣ Apply migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Create superuser
python manage.py createsuperuser

7️⃣ Run development server
python manage.py runserver

🗂 Blog Categories Seed Data

Use this query to insert default blog categories:

INSERT INTO blog_category (name) VALUES
('COVID-19'),
('Immunization'),
('Mental Health'),
('Emergency Care'),
('Child Care'),
('Nutrition'),
('General Health'),
('Medical Research');

📝 Doctor Blog CRUD Routes
Action	URL	Method
Create Blog	/blog/create/	GET/POST
List My Blogs	/blog/my-blogs/	GET
Edit Blog	/blog/edit/<id>/	GET/POST
Delete Blog	/blog/delete/<id>/	POST
🧩 Role-Based Dashboard Redirect

After login:

Doctor → /doctor/dashboard/

Patient → /patient/dashboard/

🎨 Frontend

Built with Bootstrap 5

Consistent UI across doctor & patient portals

Clean card-based blog listing

Stylish navbar with role-based links

📸 Features Preview

✔ Doctor Blog Cards
✔ Patient Blog Viewer
✔ Rich Forms with Pre-populated Edit View
✔ Role-Based Navigation Bar

(Screenshots can be added later)

🤝 Contributing

Pull requests are welcome.
Open an issue to suggest improvements or new features.
