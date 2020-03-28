import math

''' Shape is Parent Class and have attributes Color and Filled
    Attributes: Color , Filled 
    Methods: get_color()
             set_color() 
             get_filled() 
             set_filled() 
'''


class Shape:

    def __init__(self, color='black', filled=False):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled


''' Rectangle is Child Class of Shape Class and have attributes Length and Breadth
    Attributes: Length , Breadth 
    Methods: get_length()
             set_length() 
             get_breadth()
             set_breadth()
             get_area()
             get_perimeter()
              
'''


class Rectangle(Shape):

    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_breadth(self):
        return self.__breadth

    def set_breadth(self, breadth):
        self.__breadth = breadth

    def get_area(self):
        return self.__length * self.__breadth

    def get_perimeter(self):
        return 2 * (self.__length + self.__breadth)


''' Circle is Child Class of Shape Class and have attributes __radius
    Attributes: __radius 
    Methods: get_radius()
             set_radius() 
             get_area()
             get_perimeter()
'''


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius


''' Square is Child Class of Shape Class and have attributes __length
    Attributes: __length 
    Methods: get_Length()
             set_Length() 
             get_area()
             get_perimeter()
'''


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.__length = length

    def get_Length(self):
        return self.__length

    def set_Length(self, length):
        self.__length = length

    def get_area(self):
        return self.__length ** 2

    def get_perimeter(self):
        return 4 * self.__length


r1 = Rectangle(10.5, 2.5)
print('-----------------------> RECTANGLE OBJECT <----------------------')
print("Area of rectangle r1:", r1.get_area())
print("Perimeter of rectangle r1:", r1.get_perimeter())
print("Color of rectangle r1:", r1.get_color())
print("Is rectangle r1 filled ? ", r1.get_filled())
r1.set_filled(True)
print("Is rectangle r1 filled ? ", r1.get_filled())
r1.set_color("orange")
print("Color of rectangle r1:", r1.get_color())
print('-----------------------> RECTANGLE OBJECT <----------------------')

c1 = Circle(12)
print('-----------------------> CIRCLE OBJECT <-------------------------')
print("\nArea of circle c1:", format(c1.get_area(), "0.2f"))
print("Perimeter of circle c1:", format(c1.get_perimeter(), "0.2f"))
print("Color of circle c1:", c1.get_color())
print("Is circle c1 filled ? ", c1.get_filled())
c1.set_filled(True)
print("Is circle c1 filled ? ", c1.get_filled())
c1.set_color("blue")
print("Color of circle c1:", c1.get_color())
print('-----------------------> CIRCLE OBJECT <-------------------------')

sq1 = Square(5)
print('-----------------------> SQUARE OBJECT <-------------------------')
print("\nArea of Square sq1:", format(sq1.get_area(), "0.2f"))
print("Perimeter of Square sq1:", format(sq1.get_perimeter(), "0.2f"))
print("Color of Square sq1:", sq1.get_color())
print("Is Square sqr filled ? ", sq1.get_filled())
sq1.set_filled(False)
print("Is Square square filled ? ", sq1.get_filled())
sq1.set_color("blue")
print("Color of Square sq1:", sq1.get_color())
print('-----------------------> SQUARE OBJECT <-------------------------')