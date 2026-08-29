import csv
import os


class EmployeeManager:

    def __init__(self, file_path):
        self.file_path = file_path

        if not os.path.exists(file_path):
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'Name', 'Position', 'Salary', 'Email'])

            self.employees = []

        else:
            self.employees = self.load_details()

    def load_details(self):
        with open(self.file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            employees = []

            for row in reader:
                try:
                    row['ID'] = int(row['ID'])
                    row['Salary'] = int(row['Salary'])
                    employees.append(row)

                except ValueError:
                    print("Please, check the values in your file (numbers)")

            return employees

    def add_employee(self):
        try:
            id_num = int(input('Enter Your ID: '))

            for employee in self.employees:
                if employee['ID'] == id_num:
                    print('Employee Already Exists')
                    return

            name = input('Enter Your Name: ')
            position = input('Enter Your Position: ')
            salary = int(input('Enter Your Salary: '))
            email = input('Enter Your Email: ')

            new_employee = {
                'ID': id_num,
                'Name': name,
                'Position': position,
                'Salary': salary,
                'Email': email
            }

            self.employees.append(new_employee)

            print('Employee Added Successfully')

        except ValueError:
            print("Invalid, Please Enter a valid Number")

    def view_all_employees(self):
        print('\nAvailable Employees:')

        if not self.employees:
            print("No Employees Found")
            return

        for idx, employee in enumerate(self.employees, start=1):
            print(f"{idx}- {employee['Name']}")

    def update_employee(self):
        try:
            employee_id = int(input("Enter Employee ID: "))

            for employee in self.employees:

                if employee["ID"] == employee_id:

                    print("Leave field empty if you don't want to change it.")

                    name = input(f"Name [{employee['Name']}]: ")
                    position = input(f"Position [{employee['Position']}]: ")
                    salary = input(f"Salary [{employee['Salary']}]: ")
                    email = input(f"Email [{employee['Email']}]: ")

                    if name:
                        employee["Name"] = name

                    if position:
                        employee["Position"] = position

                    if salary:
                        try:
                            employee["Salary"] = int(salary)
                        except ValueError:
                            print("Invalid salary. Salary was not changed.")

                    if email:
                        employee["Email"] = email

                    print("Employee Updated Successfully")
                    return

            print("Employee not found!")

        except ValueError:
            print("Invalid Employee ID. Please enter a number.")

    def delete_employee(self):
        try:
            id_num = int(input('Enter The ID Of Employee You Want To Delete: '))

            for employee in self.employees:

                if employee['ID'] == id_num:

                    self.employees.remove(employee)

                    print(
                        f'The employee {employee["Name"]} '
                        f'(ID: {employee["ID"]}) Removed Successfully'
                    )

                    return

            print(f'Employee with ID {id_num} Not Found')

        except ValueError:
            print("Invalid ID. Please enter a number.")

    def search_employee(self):
        try:
            employee_id = int(input("Enter Employee ID: "))

            for employee in self.employees:

                if employee["ID"] == employee_id:

                    print("\nEmployee Found!")
                    print("ID:", employee["ID"])
                    print("Name:", employee["Name"])
                    print("Position:", employee["Position"])
                    print("Salary:", employee["Salary"])
                    print("Email:", employee["Email"])

                    return

            print("Employee not found!")

        except ValueError:
            print("Invalid Employee ID. Please enter a number.")

    def save_exit(self):
        with open(self.file_path, 'w', newline='') as file:

            writer = csv.DictWriter(
                file,
                fieldnames=['ID', 'Name', 'Position', 'Salary', 'Email']
            )

            writer.writeheader()
            writer.writerows(self.employees)

        print("Data Saved Successfully")

    def show_menu(self):

        while True:

            print("\n========== Employee Management System ==========")
            print("1. View All Employees")
            print("2. Add Employee")
            print("3. Remove Employee")
            print("4. Update Employee")
            print("5. Search Employee")
            print("6. Save and Exit")

            choice = input("Please, choose from options (1-6): ")

            if choice == "1":
                self.view_all_employees()

            elif choice == "2":
                self.add_employee()

            elif choice == "3":
                self.delete_employee()

            elif choice == "4":
                self.update_employee()

            elif choice == "5":
                self.search_employee()

            elif choice == "6":
                self.save_exit()
                print("Thank you for using Our system")
                break

            else:
                print("Invalid choice, Please Try Again")


if __name__ == "__main__":

    file_path = "Employees_details.csv"

    emp_1 = EmployeeManager(file_path)

    emp_1.show_menu()