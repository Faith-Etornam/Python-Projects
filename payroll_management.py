from functools import reduce

class Employee:
    def __init__(self, employee_id: str, name: str, position: str, base_salary: float):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self._base_salary = base_salary

    def calculate_pay(self):
        return self._base_salary
        
    def get_employee_info(self):
        return f"Employee #{self.employee_id} and name {self.name} has ${self._base_salary}"
    
    def __str__(self):
        return f"{self.name} at {self.position} position"


class Manager(Employee):
    def __init__(self, employee_id, name, position, base_salary, bonus):
        super().__init__(employee_id, name, position, base_salary)
        self._bonus = bonus
    
    def calculate_pay(self):
        return self._base_salary + self._bonus
    

class PayrollSystem:
    def __init__(self):
        self._employees = []

    def add_employee(self, employee):
        self._employees.append(employee)
        return f"Employee {employee.name} has been successfully added"

    def remove_employee(self, employee_num: int):
        for employee in self._employees:
            if employee.employee_id == employee_num:
                self._employees.remove(employee)
                return f"Employee #{employee.employee_id} with the name {employee.name} has been deleted successfully"
        return "Employee with employee #{employee.employee_id} has not been found"

    def calculate_total_payroll(self):
       return reduce((lambda acc, emp: acc + emp.calculate_pay()), self._employees, 0)

    def list_employees(self):
        for employee in self._employees:
            print(employee)

    def get_employee(self, employee_id):
        for employee in self._employees:
            if employee.employee_id == employee_id:
                return employee
        return f"Employee # {employee_id} not found"




payroll = PayrollSystem()

# Add employees
payroll.add_employee(Employee("E001", "John Doe", "Developer", 5000))
payroll.add_employee(Employee("E002", "Jane Smith", "Designer", 4500))
payroll.add_employee(Manager("E003", "Mike Johnson", "Team Lead", 6000, 1500))

# List all employees
print("All Employees:")
payroll.list_employees()

# Calculate total payroll
total = payroll.calculate_total_payroll()
print(f"\nTotal Payroll: ${total}")

# Remove an employee
payroll.remove_employee("E002")

print("\nAfter removing Jane Smith:")
payroll.list_employees()


        