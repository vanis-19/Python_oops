class employee():
    def __init__(self,name,age,salary):  
        self.name = name
        self.age = age
        self.salary = salary
    def display(self):
        print(self.name, self.age, self.salary)   
              
class childemployee1(employee):
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def display(self):
        print(self.name, self.age, self.salary)   
              
 
class childemployee2(childemployee1):
    def __init__(self, name, age, salary, id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id=id
    def display(self):
        print(self.name, self.age, self.salary, self.id)   
              
emp1 = employee('harshit',22,1000)
emp2 = childemployee1('arjun',23,2000)
 
emp1.display()
emp2.display()