class employee1():
    def __init__(self, name, age, salary):  
        self.name = name
        self.age = age
        self.salary = salary
    def display(self):
        print(self.name, self.age, self.salary)   
 
class childemployee(employee1):
    def __init__(self, name, age, salary,id):
        super().__init__(name,age,id)
        #self.name = name
        #self.age = age
        #self.salary = salary
        self.id = id
    def display(self):
        print(self.name, self.age, self.salary, self.id)   
          
     
emp1 = childemployee('harshit',22,1000,89)
emp1.display() 
