class BaseEmployee():
    "The base class for an employee."

    # Note: Unlike c#, on initiliazing a child class, the base contructor is not called
    # unless specifically called.
    def __init__(self, id, city):
        "Constructor for the base employee class."
        print('Base constructor called.');
        self.id = id;
        self.city = city;

    def __del__(self):
        "Will be called on destruction of employee object. Can also be called explicitly."
        print(self.__class__.__name__, 'destroyed');

    def printEmployee(self):
        print("Id:", self.id, "Name:", self.name, "City:", self.city);