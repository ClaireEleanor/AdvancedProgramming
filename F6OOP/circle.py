class Circle():
    def __init__(self, r, id):
        self.radius = r
        self.id = id

    def area(self):
        return (self.radius**2)*3.14

    def perimeter(self):
        return 2*self.radius*3.14

    def __str__(self):
        return "Circle %i has a radius of %.2f, an area of %.2f, and a perimeter of %.2f" % (self.id, self.radius, self.area(), self.perimeter())

circlist = []
while 1:
    comm = input('Enter 1 to add circle, 2 to list circles, 3 to exit: ')
    if comm == 1:
        radius = input('Enter circle radius: ')
        circlist.append(Circle(radius, len(circlist)))

    elif comm == 2:
        for i in range(0,len(circlist)):
            print circlist[i]
    elif comm == 3:
        break
