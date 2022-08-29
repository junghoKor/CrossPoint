import cv2 as cv
import numpy as np
import math


class Point(tuple):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __new__(self, x, y):
        return tuple.__new__(Point, (int(x+0.5), int(y+0.5)))
    
    def __str__(self):
        return f'({self.x},{self.y})'
        
    def __repr__(self):
        return u'Point({0}, {1})'.format(self.x, self.y)
        
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
        
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)


RED  =  (0,0,255)
BLUE =  (255,0,0)
GREEN = (0,255,0)


def rotate(origin, point, angle):
    angle = math.radians(angle)
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return Point(qx, qy)    

def get_cross_points(pt1, pt2, length):
    dif = pt2 - pt1
    angle = math.degrees( math.atan2( dif.y, dif.x ) )+ 90
    p1 = rotate (pt1, pt1+Point(length,0), angle)
    
    dif2 = pt1 - p1
    p2 = Point(pt1.x+dif2.x, pt1.y+dif2.y)
    return p1, p2


def main():
    img = np.zeros((1024, 1400, 3), dtype = "uint8")

    pt1 = Point(125,300)
    pt2 = Point(420,300)
    
    for angle in range(540):
        #img.fill(0)

        r = 200
        x = r* math.cos(math.radians(angle))+pt1.x
        y = r* math.sin(math.radians(angle))+pt1.y
        pt2 = Point(x,y)
        
        cv.line(img, pt1, pt2, BLUE,1)
        p1, p2 = get_cross_points(pt1, pt2, 100)

        cv.circle(img, p1, 3, RED, 1)
        cv.circle(img, p2, 3, RED, 1)
        
        cv.line(img, p1, p2, GREEN,1)
        
        pt1 = pt1 + Point(2,0)
        pt2 = pt2 + Point(2,0)

        cv.imshow('View', img)
        cv.waitKey(5)
    cv.waitKey(0)
    
	
main()