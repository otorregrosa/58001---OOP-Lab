class Circle():
    def diameter(self, diameter):
        d = diameter
    def radius(self, radius):
        r = radius
    def area(self,d):
        area = (d/2)^2 * 3.14
        print("Area of the circle is: ",area)
    def peri(self,d):
        peri = 3.14 * r
        print("Perimeter of the circle is: ",peri)
    def area(self,r):
        area = 3.14 * r * r
        print("Area of the circle is: ",area)
    def peri(self,r):
        peri = 2 * 3.14 * r
        print("Perimeter of the circle is: ",peri)

c = Circle()
radius = int(input("Enter the radius of the circle: "))
diameter = int(input("Enter the diameter of the circle: "))
c.area(radius)
c.peri(radius)
c.area(diameter)
c.peri(diameter)