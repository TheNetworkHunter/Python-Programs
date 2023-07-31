# Simple Employee Management System using SQLite DB designed by Hunter Laberge

import sqlite3
class Database:
    def __init__(self):
        # Establish a connection to the SQLite database
        self.conn = sqlite3.connect('employee.db')
        self.cursor = self.conn.cursor()

        # Create the employees table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                               (id TEXT PRIMARY KEY,
                                name TEXT,
                                age INTEGER,
                                department TEXT,
                                position TEXT)''')

    def add_employee(self, employee):
        # Insert employee data into the employees table
        self.cursor.execute('''INSERT INTO employees (id, name, age, department, position)
                               VALUES (?, ?, ?, ?, ?)''',
                            (employee['id'], employee['name'], employee['age'], employee['department'], employee['position']))
        self.conn.commit()

    def find_employee(self, employee_id):
        # Retrieve an employee with the specified ID from the employees table
        self.cursor.execute('SELECT * FROM employees WHERE id = ?', (employee_id,))
        employee = self.cursor.fetchone()
        if employee:
            return {
                'id': employee[0],
                'name': employee[1],
                'age': employee[2],
                'department': employee[3],
                'position': employee[4]
            }
        else:
            return None

    def edit_employee(self, employee_id, new_data):
        # Update employee data in the employees table
        self.cursor.execute('''UPDATE employees
                               SET name = ?, age = ?, department = ?, position = ?
                               WHERE id = ?''',
                            (new_data['name'], new_data['age'], new_data['department'], new_data['position'], employee_id))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def remove_employee(self, employee_id):
        # Delete an employee from the employees table
        self.cursor.execute('DELETE FROM employees WHERE id = ?', (employee_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0


def employee_management_system():
    database = Database()

    while True:
        print("***** Employee Management System *****")
        print("1.) Add Employee")
        print("2.) Find Employee")
        print("3.) Edit Employee")
        print("4.) Remove Employee")
        print("5.) Exit Application")

        choice = input("Select an option: ")

        if choice == "1":
            add_employee(database)
        elif choice == "2":
            find_employee(database)
        elif choice == "3":
            edit_employee(database)
        elif choice == "4":
            remove_employee(database)
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Make sure to only use numbers (1-5).")

    # Close the connection to the SQLite database
    database.conn.close()


# Run the employee management system
employee_management_system()
