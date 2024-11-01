# Study Buddy

A web application for managing and displaying student data, developed using Django. This app features a searchable student list with pagination, detailed student information pages, and automated data seeding for testing purposes.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Admin Interface](#admin-interface)
- [Dependencies](#dependencies)


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
    > python manage.py runserver

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




