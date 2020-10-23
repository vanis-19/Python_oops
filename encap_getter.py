class year_graduated:
   def __init__(self, year=0):
      self.__year = year

   # getter method
   def display(self):
      return self.__year

# setter method
   #def set_year(self, a):
       #self._year = a

grad_obj = year_graduated()
# Before using setter
print(grad_obj.display())

# After using setter
#grad_obj.set_year(2019)
#print(grad_obj._year)