# Uebung 3: Objektorientierung 3

# Aufgabe 1 Vererbung

import math


class Figur:
    def __init__ (self,name):
        self.name = name

    def umfang(self):
        return 0

    def __str__ (self):
        return self.name
    
class Punkt:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Punkt ({self.x}, {self.y})"



class Dreieck(Figur):
    def __init__ (self,p1,p2,p3):
        super().__init__("Dreieck")
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__ (self):
        return f"{self.name} mit {self.p1}, {self.p2}, {self.p3}"
    
    def umfang(self):
        self.d1 = math.sqrt((self.p2.y - self.p1.y)**2 + (self.p2.x - self.p1.x)**2)
        self.d2 = math.sqrt((self.p3.y - self.p2.y)**2 + (self.p3.x - self.p2.x)**2)
        self.d3 = math.sqrt((self.p1.y - self.p3.y)**2 + (self.p1.x - self.p3.x)**2)
        return round(self.d1 + self.d2 + self.d3, 3)


class Rechteck(Figur):
    def __init__(self,p1,p2):
        super().__init__("Rechteck")
        self.p1 = p1
        self.p2 = p2

    def __str__ (self):
        return f"{self.name} mit {self.p1} - {self.p2}"
    
    def umfang(self):
        self.r1 = abs(self.p2.y - self.p1.y)
        self.r2 = abs(self.p2.x - self.p1.x)
        return round(2 * (self.r1 + self.r2), 3)


class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def __str__ (self):
        return f"{self.name} M = {self.mittelpunkt} und r = {self.radius}"

    def umfang(self):
        return round(math.pi * self.radius * 2, 3)


# Weiss nicht wie ich das mit dem Polygon machen muss
'''class Polygon(Figur):
    def __init__(self, p):
        super().__init__("Polygon")
        self.p = p

    def Umfang(self):
        return 0
    
    def __str__(self):
        return f"{self.name} mit {self.p}"'''
    


# Abfrage

A = Punkt(1.5,-2.6)
B = Punkt(-3.2,2.4)
C = Punkt(6,5.3)
D = Punkt(1.8,8.8)


# Dreieck
'''
d = Dreieck(A,B,C)
print (d)
print (d.umfang ())
'''

# Rechteck
'''
r = Rechteck(A,B)
print (r)
print (r.umfang ())
'''

# Kreis
'''
k = Kreis(A, 10)
print (k)
print (k.umfang ()) 
'''

# Polygon
'''
p = Polygon(A,B,C,D)
print(p)
print(p.Umfang())
'''