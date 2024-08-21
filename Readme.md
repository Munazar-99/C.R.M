# CRM Web Application

A simple Customer Relationship Management (CRM) web application built using Django and MySQL. This application allows you to manage customer information, view customer lists, and perform basic CRM operations.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running Migrations](#running-migrations)
- [Running the Application](#running-the-application)


## Features

- **Customer Management**: Add, update, delete, and view customers.
- **User Authentication**: Secure login system using Django's built-in authentication.
- **Responsive UI**: Simple and intuitive user interface that works on different devices.
- **Database**: Uses MySQL to store customer data.

## Installation

Follow these steps to set up and run the application locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/crm-web-app.git
   cd crm-web-app
   ```

## Database Setup

1. **Create a MySQL database**:

   Open MySQL Workbench or your preferred MySQL client and run the following command:

   ```sql
   CREATE DATABASE crm;
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`

   ```

   3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

   ```

3. **Configure Database Connection:**

   Update the `DATABASES` setting in `crm_project/settings.py` to connect to your MySQL database. Use the following configuration as an example:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'crm_db',
           'USER': 'your_mysql_user',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

   Replace 'crm_db', 'your_mysql_user', and 'your_mysql_password' with your actual database name, MySQL username, and password, respectively.

4. **Apply Migrations:**

   After configuring the database, apply the migrations to set up the initial database schema:

   ```bash
   python manage.py migrate
   ```

   This command will create the necessary tables and relationships in your MySQL database based on the models defined in your Django application.

   4. **Create a Superuser:**

   To access the Django admin panel, create a superuser account by running:

   ```bash
   python manage.py createsuperuser
   ```

   5. **Run the Development Server:**

   Start the Django development server to launch your application:

   ```bash
   python manage.py runserver
   ```
