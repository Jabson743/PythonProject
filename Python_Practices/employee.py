class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


emp_1 = Employee('Harry', 'Smith', '500')
print(Employee.get_full_name(emp_1))