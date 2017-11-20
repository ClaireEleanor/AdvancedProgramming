class Circle():
    def __init__(self, r):
        self.x = r

    def area(self):
        return (self.x**2)*3.14

    def perimeter(self):
        return 2*self.x*3.14

    def __str__(self):
        return "Circle has a radius of %.2f, an area of %.2f, and a perimeter of %.2f" % (self.x, self.area(), self.perimeter())
