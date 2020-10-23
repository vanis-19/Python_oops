class employee(object):
    def __init__(self):   
        self.name = 1234
        self._age = 1234
        self.__salary = 1234
 
object1 = employee()
print(object1.name)
print(object1._age)
print(object1.__salary)