# Employee Management System

This Employee Management System is a web application built using Streamlit and MySQL. It allows admins to manage employee records, including adding, viewing, updating, and deleting employee data. It also includes functionalities for employee login and authentication.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Database Setup](#database-setup)
6. [Running the Application](#running-the-application)
7. [Usage](#usage)
8. [Screenshots](#screenshots)
9. [Troubleshooting](#troubleshooting)

---

### Features

- **Admin Login and Authentication**: Restrict access to the admin panel and functionalities based on user roles.
- **Employee Data Management**: Add, view, update, and delete employee records with details such as ID, name, phone, position, gender, and salary.
- **Search Functionality**: Search employees based on various criteria like ID, name, position, and gender.
- **Payroll and Attendance Tracking**: Manage payroll and attendance (if implemented in the future).
- **Statistics and Reporting**: Generate reports and view statistics like total employees, average salary, etc. (optional).

### Technologies Used

- **Frontend**: Streamlit (Python)
- **Backend**: MySQL
- **Database Library**: PyMySQL

---

### Prerequisites

1. **Python 3.7+**
2. **MySQL Server** (with access to create and manage databases)
3. Required Python packages:
   - `streamlit`
   - `pymysql`
   - `pandas`

Install the packages using:
```bash
pip install streamlit pymysql pandas
```

---

### Installation

1. Clone or download the repository.
2. Navigate to the project directory.
3. Set up the database and create tables as shown below.

### Database Setup

1. **Create Database**: Open your MySQL command line or a MySQL GUI (like MySQL Workbench) and create the `employee_management` database:
   ```sql
   CREATE DATABASE employee_management;
   ```

2. **Create Tables**:
   - Create a `users` table to store login credentials and roles:
     ```sql
     CREATE TABLE users (
         username VARCHAR(50) PRIMARY KEY,
         password VARCHAR(50),
         role ENUM('admin', 'employee') NOT NULL
     );
     ```
   - Create the `view_employee` table to store employee information:
     ```sql
     CREATE TABLE view_employee (
         emp_id VARCHAR(10) PRIMARY KEY,
         name VARCHAR(50),
         phone VARCHAR(15),
         position VARCHAR(50),
         gender ENUM('Male', 'Female', 'Other'),
         salary DECIMAL(10, 2)
     );
     ```

3. **Insert Initial Admin User** (optional for initial testing):
   ```sql
   INSERT INTO users (username, password, role) VALUES ('admin', 'admin123', 'admin');
   ```

---

### Running the Application

1. **Start MySQL Server**:
   Ensure your MySQL server is running locally.

2. **Run Streamlit Application**:
   Open a terminal in the project directory and execute:
   ```bash
   streamlit run app.py
   ```
3. **Access the Application**:
   After the command executes, a URL will appear in the terminal. Click on it or navigate to it in a web browser to access the app.

---

### Usage

1. **Login**:
   - **Admin**: Log in with the username and password configured in the database. Admins can manage employee records fully.
   - **Employee**: Limited access to view or update their own details (if implemented).

2. **Admin Functionalities**:
   - **View Employee Data**: View a table of all employees.
   - **Add Employee**: Fill out a form to add a new employee.
   - **Search Employee**: Select search criteria and input a value to search for specific employees.
   - **Update Employee**: Update details for a specific employee.
   - **Delete Employee**: Delete a specific employee by entering their Employee ID.
   - **Delete All**: Delete all employee records from the database (use carefully).

3. **Logout**: To log out, simply restart the app.

---

### Screenshots

1. **Login Screen**: Allows admins and employees to log in.
   ![image](https://github.com/user-attachments/assets/728a3d51-eb02-4307-8793-c91e5a04b6c7)

2. **Admin Dashboard**: Shows navigation options like "View Employee Data," "Add Employee," etc.
  ![image](https://github.com/user-attachments/assets/f0cdfdf6-027a-4b6c-adfa-8aefab291b02)
   
3. **Add Employee**: Form to add new employee records.
   ![image](https://github.com/user-attachments/assets/9d5d5022-c10d-4c21-9220-819cebfc4570)

4. **Delete Employee**: Enter an Employee ID to delete a specific record.
   ![image](https://github.com/user-attachments/assets/a27a8a05-2f0e-4150-a6df-027a8298aca8)


---

### Troubleshooting

- **Database Connection Issues**: Ensure MySQL is running and that the connection details in `backend.py` match your setup.
- **Error Messages**:
  - *Invalid Employee ID*: Make sure you enter a valid ID in the "Delete Employee" section.
  - *Login Failure*: Check that the username and password are correct in the `users` table.
- **Permissions**: Ensure that MySQL user `root` (or your MySQL username) has the necessary permissions.

---

