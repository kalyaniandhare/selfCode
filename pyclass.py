class Employee:
    count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def getEmpCount(self):
        print Employee.count

    def getEmpInfo(self):
        print "Info", self.name, self.salary


emp1 = Employee("kalyani", "75000")
emp2 = Employee("Sarthak", "5500")

emp1.getEmpInfo()
emp2.getEmpInfo()
emp1.getEmpCount()
emp2.getEmpCount()
emp1.age = 7
print(emp1)
print(hasattr(emp1 , 'age'))
setattr(emp1, 'test', 'exam1')
print(hasattr(emp1 , 'test'))
print(getattr(emp1 , 'name'))
print(delattr(emp1 , 'age'))
print Employee.count


