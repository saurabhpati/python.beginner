from base_employee import BaseEmployee;
class Manager(BaseEmployee):
    
    def __init__(self, name):
        self.designation = 'Manager';
        self.name = name;

    # This printEmployee method is overriden from BaseEmployee.
    def printEmployee(self):
        if hasattr(self, 'id'):
            print('Id:', self.id, 'Name:', self.name, 'designation:', self.designation);
        else:
            print('Name:', self.name, 'Designation:', self.designation);
            
        