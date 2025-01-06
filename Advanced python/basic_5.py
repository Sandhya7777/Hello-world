'''
1. class
2. object

__init__(self)
'''

class Base:

    def __init__(self, side_one, side_two, side_three):
        self.side_one = int(side_one)   
        self.__side_two = int(side_two)
        self.__side_three = int(side_three)

    def perimeter(self):
        perimeter = self.side_one + self.__side_two + self.__side_three
        return perimeter

class Main(Base):
    def __init__(self, side_one, side_two, side_three):
        Base.__init__(self, side_one, side_two, side_three)
    
    def display(self):
        value = Base.perimeter(self)
        print(type(self.side_one))
        print(f"value of the perimeter is : {value}")

name = Main("5","2","3")
name.display()