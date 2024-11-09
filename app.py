# app.py
import streamlit as st
import pandas as pd
import backend as db  # Assuming backend has the required functions

# Initialize session state for role and username if not set
if "role" not in st.session_state:
    st.session_state["role"] = None
if "username" not in st.session_state:
    st.session_state["username"] = None

# Sidebar navigation
st.sidebar.title("Employee Management System")
page = st.sidebar.radio("Navigate", ["Login", "Admin Panel"])

# Database connection
db.connect()

# Login Section
if page == "Login":
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        role = db.authenticate(username, password)
        if role:
            st.session_state["role"] = role
            st.session_state["username"] = username
            st.sidebar.success(f"Logged in as {role}")
        else:
            st.error("Invalid credentials")

# Admin Panel Section
if page == "Admin Panel":
    if st.session_state["role"] == "admin":
        st.header("Admin Panel")

        # Sidebar Navigation for Admin Functionalities
        nav = st.sidebar.radio("Navigation", ['View Employee Data', 'Add Employee', 'Search Employee', 'Update Employee', 'Delete Employee', 'Delete All'])
        st.title("Employee Management System")

        # View Employee Data
        if nav == 'View Employee Data':
            st.header("Employee Data")
            employees = db.fetch_employee()
            
            if employees:
                df = pd.DataFrame(employees, columns=["ID", "Name", "Phone", "Role", "Gender", "Salary"])
                st.table(df)
            else:
                st.write("No employee data available.")

        # Add Employee
        elif nav == 'Add Employee':
            st.header("Enter New Employee Details")
            emp_id = st.text_input("Employee ID")
            name = st.text_input("Name")
            phone = st.number_input("Phone", min_value=0, format="%d")

            position = st.selectbox("Position", [
                "Application Developer", "Business Analyst", "Cloud Engineer", 
                "Data Analyst", "Data Engineer", "Data Scientist", "Database Administrator", 
                "DevOps Engineer", "Full Stack Developer", "Helpdesk Support", 
                "Information Security Analyst", "Infrastructure Engineer", "IT Consultant", 
                "Mobile Application Developer", "Network Engineer", "Project Manager", 
                "QA Engineer", "Scrum Master", "Software Engineer", "Solution Architect", 
                "Systems Analyst", "Technical Lead", "Technical Support Engineer", 
                "Test Automation Engineer", "UI/UX Designer", "Web Developer"
            ])
            
            gender = st.radio("Gender", ["Male", "Female", "Other"])
            salary = st.number_input("Salary", min_value=0.0, format="%f")
            
            if st.button("Add Employee"):
                db.add_employee(emp_id, name, phone, position, gender, salary)
                st.success("Employee added successfully!")

        # Search Employee
        elif nav == 'Search Employee':
            st.header("Search Employee")
            search_field = st.selectbox("Search by", ["ID", "Name", "Phone", "Position", "Gender", "Salary"])
            
            if search_field == "Position":
                search_value = st.selectbox("Select Position", [
                    "Application Developer", "Business Analyst", "Cloud Engineer", 
                    "Data Analyst", "Data Engineer", "Data Scientist", "Database Administrator", 
                    "DevOps Engineer", "Full Stack Developer", "Helpdesk Support", 
                    "Information Security Analyst", "Infrastructure Engineer", "IT Consultant", 
                    "Mobile Application Developer", "Network Engineer", "Project Manager", 
                    "QA Engineer", "Scrum Master", "Software Engineer", "Solution Architect", 
                    "Systems Analyst", "Technical Lead", "Technical Support Engineer", 
                    "Test Automation Engineer", "UI/UX Designer", "Web Developer"
                ])
            elif search_field == "Gender":
                search_value = st.radio("Select Gender", ["Male", "Female", "Other"])
            else:
                search_value = st.text_input(f"Enter {search_field}")

            if st.button("Search"):
                if search_value:
                    field_mapping = {
                        "ID": "emp_id",
                        "Name": "name",
                        "Phone": "phone",
                        "Position": "position",
                        "Gender": "gender",
                        "Salary": "salary"
                    }
                    search_field_db = field_mapping.get(search_field, search_field.lower())
                    results = db.search_employee(search_field_db, search_value)

                    if results:
                        df_results = pd.DataFrame(results, columns=["ID", "Name", "Phone", "Position", "Gender", "Salary"])
                        st.dataframe(df_results)
                    else:
                        st.warning("No employees found with the specified criteria.")
                else:
                    st.error(f"Please enter a valid {search_field} to search.")

        # Update Employee
        elif nav == 'Update Employee':
            st.header("Update Employee Data")
            emp_id = st.text_input("Enter Employee ID to Update")
            
            if emp_id:
                if db.id_exists(emp_id):
                    update_field = st.selectbox("Select Field to Update", ["Name", "Phone", "Position", "Gender", "Salary"])
                    if update_field == "Position":
                        new_value = st.selectbox("Select Position", [
                        "Application Developer", "Business Analyst", "Cloud Engineer", 
                        "Data Analyst", "Data Engineer", "Data Scientist", "Database Administrator", 
                        "DevOps Engineer", "Full Stack Developer", "Helpdesk Support", 
                        "Information Security Analyst", "Infrastructure Engineer", "IT Consultant", 
                        "Mobile Application Developer", "Network Engineer", "Project Manager", 
                        "QA Engineer", "Scrum Master", "Software Engineer", "Solution Architect", 
                        "Systems Analyst", "Technical Lead", "Technical Support Engineer", 
                        "Test Automation Engineer", "UI/UX Designer", "Web Developer"])

                    elif update_field == "Gender":
                        new_value = st.radio("Select Gender", ["Male", "Female", "Other"])

                    else:
                        new_value = st.text_input(f"Enter new{update_field}")
                    
                    if st.button("Update Employee"):
                        if new_value:
                            db.update_employee_field(emp_id, update_field.lower(), new_value)
                            st.success(f"{update_field} updated successfully for Employee ID: {emp_id}")
                        else:
                            st.error("Please enter a valid value to update.")
                else:
                    st.warning("Employee ID not found. Please enter a valid ID.")

        # Delete Employee
        elif nav == 'Delete Employee':
            st.header("Delete Employee")
            emp_id = st.text_input("Employee ID to Delete")
    
            if emp_id:
                if db.id_exists(emp_id):  # Check if the Employee ID exists
                    if st.button("Delete Employee"):
                        db.delete_employee(emp_id)
                        st.success("Employee data deleted")
                else:
                    st.warning("Employee ID not found. Please enter a valid ID.")


        # Delete All Employees
        elif nav == 'Delete All':
            st.header("Delete All Employees")
            if st.button("Delete All Employees"):
                db.delete_all_records()
                st.success("All employee records deleted!")

    else:
        st.warning("Please log in as an admin to access this page.")
