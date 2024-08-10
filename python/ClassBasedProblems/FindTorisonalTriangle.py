
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __sub__(self, no):  # subtract both points , no is seconde point and self is first point
        x,y,z=self.x-no.x , self.y - no.y , self.z- no.z
        return Points(x,y,z)  # return point object of cordinates x,y,z
    
    # x.y = x1x2 + y1y2 + z1z2
    def dot(self, no):
        dot_product= self.x*no.x  + self.y*no.y + self.z*no.z
        return  dot_product
    def cross(self, no):
        # formula used - A × B = (a1b2 - a2b1)i + (a3b1 - a1b3)j + (a2b3 - a3b2)k
        a=self.x*no.y  - self.y*no.x
        b=self.z*no.x  - self.x*no.z
        c=self.y*no.z  - self.z*no.y

        return Points(a,b,c)
    
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)  # return  magnitude of a point of coordinates

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))