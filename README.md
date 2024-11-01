# Study Buddy

A web application for managing and displaying student data, developed using Django. This app features a searchable student list with pagination, detailed student information pages, and automated data seeding for testing purposes.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Admin Interface](#admin-interface)
- [Dependencies](#dependencies)

<img width="800" height="auto" alt="Screenshot 2024-11-01 at 10 47 08 PM" src="https://github.com/user-attachments/assets/60b5e642-8779-4e7f-bacc-fca43747f5ac">
<img width="800" height="auto" alt="Screenshot 2024-11-01 at 10 47 23 PM" src="https://github.com/user-attachments/assets/092873b1-c266-40fd-93ca-22d114f7451a">
<img width="800" height="auto" alt="Screenshot 2024-11-01 at 10 47 50 PM" src="https://github.com/user-attachments/assets/957aa490-8064-4046-84f2-745950371641">



## Features
- **Student Search and Filter**: Search by name, age, department, email, or ID.
- **Pagination**: Results are paginated for easy navigation through student records.
- **Student Details View**: Detailed view showing individual student marks and rank.
- **Data Seeding**: Generate random student and report card data for testing.
- **Admin Interface**: Manage and view student data via Django's admin dashboard.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/study_buddy.git
   cd study_buddy

2. **Create and Activate a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  

3. **Run Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

4. **Create a Superuser (for the admin interface)**:
    ```bash
    python manage.py createsuperuser

5. **Start the Development Server**:
    ```bash
    python manage.py runserver

## Usage

- **Home Page**: View and search through the student records.
- **Student Detail Page**: Access individual student marks and ranking by clicking on a student ID.
- **Admin Dashboard**: Manage student data at `/admin` with the superuser credentials.


## Admin Interface

The Django admin interface provides an easy way to manage students, departments, and report cards:

- **Student Model**: View, add, and update student details.
- **Subject Marks Model**: Track individual subject marks.
- **Report Card Model**: View ranks and total marks for each student.

## Dependencies

- **Django**: Python web framework for backend.
- **Faker**: Library for generating random student data.




