# This is an encapsulation program

class Employee:
    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount


emp = Employee()
print("Old Salary:", emp.get_salary())

emp.set_salary(60000)
print("Updated Salary:", emp.get_salary())
