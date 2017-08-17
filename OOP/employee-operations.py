from employee import Employee; # importing the Employee class from employee module.

emp = Employee('Saurabh', 44444); # initializing the class by calling the constructor.
emp.printEmployee(); # calling the print employee method on emp object;

print(hasattr(emp, 'name')); # Output: True since 'name' attribute is present on the employee.
print(hasattr(emp, 'age')); # False since the 'age' attribute is not defined on employee.
setattr(emp, 'age', 24); # Will create an attribute called 'age' if not already present and assign its value.
print(getattr(emp, 'age')); # Will get the value of the attribute 'age' on the emp object only. 
print(emp.__doc__); # Will get the doc string of the employee.
print(emp.__dict__); # Will represent the emp object as a dictionary.
print(Employee.__name__); # Will get the name of the class.
print(Employee.__module__); # Will get the module to which this class belongs to.
print(Employee.__bases__); # Will get the base classes of Employee.