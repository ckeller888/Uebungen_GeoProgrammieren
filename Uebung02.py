# Uebung 2: Objektorientierung 2

# Aufgabe 1 Magische Methoden

class Vector3:
    def __init__(self,x=0.0, y=0.0, z=0.0):
        self.x=x
        self.y=y
        self.z=z

    # Konversion zu Zeichenkette
    def __str__ (self):
        return f"({self.x},{self.y},{self.z})"
    

    # Addition
    def __add__ (self, other):

        if type(other) == int or type(other) == float:
            return Vector3(self.x + other, self.y + other, self.z + other)
        
        else:
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        
    def __radd__(self, other):
        return Vector3(self.x + other, self.y + other, self.z + other)


    # Subtraktion
    def __sub__ (self, other):
        
        if type(other) == int or type(other) == float:
            return Vector3(self.x - other, self.y - other, self.z - other)
        
        else:
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        
    def __rsub__(self, other):
        return Vector3(other - self.x, other - self.y, other - self.z)
    

    # Methode cross
    def cross (self, other):
        crossx = self.y * other.z - self.z * other.y
        crossy = self.z * other.x - self.x * other.z
        crossz = self.x * other.y - self.y * other.x
        return Vector3 (crossx, crossy, crossz)
    

    # Kreuzprodukt
    def __mul__ (self, other):
        return self.cross (other)


    # Methode dot
    def dot (self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)
    
    
    # Multiplikation mit Skalar
    def __mul__ (self, other):
        return self.dot (other)


    # komponentenweise Multiplikation oder mit Zahl
    def __mul__ (self, other):
        
        if type(other) == int or type(other) == float:
            return Vector3(self.x * other, self.y * other, self.z * other)
        
        else:
            return self.cross (other)
        
    def __rmul__ (self, other):
        return Vector3(other * self.x, other * self.y, other * self.z)
   
        
    # Vektor normieren
    def normalize (self):
        normalize = (1/((self.x**2 + self.y**2 + self.z**2)**0.5))
        return Vector3(normalize*self.x, normalize*self.y, normalize*self.z)
    


# Abfrage

a = Vector3(3,4,2)
b = Vector3(2,1,0)


# Konversion Zeichenkette
'''
s = str(a)
print (s)
'''

# Addition
'''
c = a + bx
print(c)

c = b + 3
print(c)
'''
  
# Subtraktion
'''
c = a - b
print(c)

w = 10 - a
print (w)
'''

# Multilpikation mit Zahl
'''
g = 2 * a
print (g)
'''

# komponentenweise Multiplikation
'''
c = a * b
print(c)
'''

# Skalarprodukt
'''
d = a.dot(b)
print(d)
'''

# Kreuzprodukt
'''
e = a.cross(b) # Kreuzprodukt
print(e)
'''

# Vektor normieren
'''
f = Vector3.normalize(a)
print (f)
'''