# https://replit.com/@VincentEdwards1/boilerplate-polygon-area-calculator

# This is a project from freecodecamp.org. 
# It contains a Rectangle class and a Square child class. 
# Instances of the Rectangle class are initialized with width and height attributes and have methods 
# set_width, set_height, get_area, get_perimeter, get_diagonal, get_picture, and get_amount_inside. 
# Instances of the Square class are initialized with a side attribute and have an additional set_side method. 


class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)
    
    def set_width(self, width):
        '''Set the width of the rectangle to the argument.'''
        self.width = width

    def set_height(self, height):
        '''Set the height of the rectangle to the argument.'''
        self.height = height

    def get_area(self):
        '''Return the area of the rectangle.'''
        return self.width * self.height

    def get_perimeter(self):
        '''Return the perimeter of the rectangle.'''
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        '''Return the length of the diagonal of the rectangle.'''
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self) -> str:
        '''Return a string that represents the shape of the rectangle using lines of "*". The max size is 50 x 50.'''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return (('*' * self.width + '\n') * self.height)

    def get_amount_inside(self, rect) -> int:
        '''Return the number of times the argument rectangle/square could fit inside the initial rectangle/square with no rotations.'''
        return (self.width // rect.width) * (self.height // rect.height)
    
    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        self.set_side(side)

    def set_side(self, side):
        '''Set the side of the square to the argument.'''
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        '''Set the width of the square to the argument. (Also sets the height to the same amount.)'''
        self.set_side(width)

    def set_height(self, height):
        '''Set the height of the square to the argument. (Also sets the width to the same amount.)'''
        self.set_side(height)

    def __repr__(self):
        return f'Square(side={self.side})'


if __name__ == '__main__':
    rect = Rectangle(5, 10)
    print(rect.get_area())
    rect.set_width(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())
