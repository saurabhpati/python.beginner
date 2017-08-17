# This is an Employee class where class keyword is used.
from base_employee import BaseEmployee;
# BaseEmployee is Employee's base class, this is the way to have inheritance in python.
class Employee(BaseEmployee): 
    "Contains information for an employee."
    def __init__(self, id, name, salary):
        "Constructor to initialize the Employee class with his/her name and salary"
        self.id = id;
        self.name = name;
        self.salary = salary;
        print('Employee Created');
    
    def printEmployee(self):
        "Prints the employee name and salary."
        print('Name', self.name, 'Salary', self.salary);