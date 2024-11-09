import pymysql
from pymysql.constants import CLIENT
import pandas as pd

def connect():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="181818",
        database="employee_management",
        client_flag=CLIENT.MULTI_STATEMENTS
    )

# Authentication function for the app
def authenticate(username, password):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# View all employees
def fetch_employee():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT emp_id, name, phone, position, gender, salary FROM view_employee")
    data = cursor.fetchall()
    conn.close()
    return data

# Add a new employee
def add_employee(emp_id, name, phone, position, gender, salary):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO view_employee (emp_id, name, phone, position, gender, salary) VALUES (%s, %s, %s, %s, %s, %s)",
                   (emp_id, name, phone, position, gender, salary))
    conn.commit()
    conn.close()

# Search employee by specific field
# Search employee by specific field
def search_employee(field, value):
    conn = connect()
    cursor = conn.cursor()
    
    # Adjusting field for valid columns like 'emp_id', 'name', etc.
    if field not in ['emp_id', 'name', 'phone', 'position', 'gender', 'salary', 'id']:  

        raise ValueError(f"Invalid field: {field}")
    
    query = f"SELECT emp_id, name, phone, position, gender, salary FROM view_employee WHERE {field} = %s"
    cursor.execute(query, (value,))
    results = cursor.fetchall()
    conn.close()
    return results


# Check if an employee ID exists
def id_exists(emp_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM view_employee WHERE emp_id = %s", (emp_id,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

# Update a specific field of an employee record
def update_employee_field(emp_id, field, new_value):
    conn = connect()
    cursor = conn.cursor()
    query = f"UPDATE view_employee SET {field} = %s WHERE emp_id = %s"
    cursor.execute(query, (new_value, emp_id))
    conn.commit()
    conn.close()

# Delete a specific employee by ID
def delete_employee(emp_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM view_employee WHERE emp_id = %s", (emp_id,))
    conn.commit()
    conn.close()

# Delete all employee records
def delete_all_records():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM view_employee")
    conn.commit()
    conn.close()
