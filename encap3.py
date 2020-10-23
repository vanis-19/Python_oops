class ComplexNumber:
    def __init__(self, r=2, i=3):
        self.__real = 2
        self.__imag = 3

    def data(self):
        print(f'{self.__real}+{self.__imag}j')

    #def get_data(self):
    #    print(f'{self.__real}+{self.__imag}j')    


# Create a new ComplexNumber object
num1 = ComplexNumber()

# Call get_data() method
# Output: 2+3j
#num1.get_data()
num1.data()
