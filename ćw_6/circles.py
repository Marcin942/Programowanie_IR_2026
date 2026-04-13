import math
import sys

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r  

    def Circumference(self):
        return 2 * math.pi * self.r

    def Intersection(self, other):
        '''
        Zwraca liczbę punktów przecięcia dwóch okręgów
        '''
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        if distance > self.r + other.r: # okręgi są rozłączne
            return 0
        elif distance == 0 and self.r == other.r: # okręgi nachodzą na siebie
            return math.inf
        elif distance == self.r + other.r: # okręgi styczne zewnętrznie
            return 1
        elif distance == abs(self.r - other.r): # okręgi styczne wewnętrznie
            return 1
        elif distance < abs(self.r - other.r): # jeden okrąg wewnątrz drugiego, brak punktów przecięcia
            return 0
        else:
            return 2  # okręgi przecinają się w dwóch punktach
        

x1, y1, r1 = sys.argv[1], sys.argv[2], sys.argv[3]
x2, y2, r2 = sys.argv[4], sys.argv[5], sys.argv[6]

circle1 = Circle(float(x1), float(y1), float(r1))
circle2 = Circle(float(x2), float(y2), float(r2))

print(f'Obwód okręgu 1: {circle1.Circumference()}')
print(f'Obwód okręgu 2: {circle2.Circumference()}')
print(f'Liczba punktów przecięcia: {circle1.Intersection(circle2)}')