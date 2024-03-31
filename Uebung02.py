# Uebung 2: Objektorientierung 2

# Aufgabe 1 Magische Methoden

class Vector3:
    def __init__(self,x=0.0, y=0.0, z=0.0):
        self.x=x
        self.y=y
        self.z=z

    #Konversion zu Zeichenkette
    def __str__ (self):
        return f"({self.x},{self.y},{self.z})"

    #Addition
    def __add__ (self, other):

        if type(other) == int or type(other) == float:
            return Vector3(self.x + other, self.y + other, self.z + other)
        
        else:
            return Vector3(self.x + other.x, self.y + other.y, self.z + other)
        
    def __radd__(self, other):
        return Vector3(self.x + other, self.y + other, self.z + other)


    #Subtraktion
    def __sub__ (self, other):
        
        if type(other) == int or type(other) == float:
            return Vector3(self.x - other, self.y - other, self.z - other)
        
        else:
            return Vector3(self.x - other.x, self.y - other.y, self.z - other)
        
    def __radd__(self, other):
        return Vector3(self.x - other, self.y - other, self.z - other)


    #komponentenweise Muliplikation
    def __mul__ (self, other):
    
        if type(other) == int or type(other) == float:
            return Vector3(self.x * other, self.y * other, self.z * other)
    
        else:
            return Vector3(self.x * other.x, self.y * other.y, self.z * other)
    
    def __radd__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other)



    #Multiplikation mit Skalar
    def __mul__ (self, other):
        
        if type(other) == int or type(other) == float:
            return Vector3(self.x * other + self.y * other + self.z * other)
        
        else:
            return Vector3(self.x * other.x + self.y * other.y + self.z * other)
        
    def __radd__(self, other):
        return Vector3(self.x * other + self.y * other + self.z * other)



# Abfrage
# dot 10 
# -2 -5

a = Vector3(3,4,2)
b = Vector3(2,1,0)
c = a * b # Komponentenweise Multiplikation
print(c)
d = a.dot(b) # Skalarprodukt
# e = a.cross(b) # Kreuzprodukt



a = Vector3(3,4,2)
b = Vector3(2,1,0)


v1 = Vector3(-3,-4)
v2=Vector3(-4,5)


v4=v1+v2

print(v4)

print((v1-v2))

v5=Vector3(7,8)
v6= v5+1
print(v6)