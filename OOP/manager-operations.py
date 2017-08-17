# This explains the method overriding
from manager import Manager;
from base_employee import BaseEmployee;

# initializing the manager class.
mgr = Manager('Saurabh');
mgr.id = 2;
mgr.printEmployee(); # calls the method of the child class.

# initializing the base class.
emp = BaseEmployee(2, 'Greater Noida');
emp.name = 'Saurabh';
emp.printEmployee(); # calls the method of the base class.