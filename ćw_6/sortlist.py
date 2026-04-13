import sys

class SortedList:
    def __init__(self):
        self.list = []

    def append(self, value):
        '''Dodaje element do listy'''
        self.list.append(value)
        self.list.sort()

    def clear(self):
        '''Usuwa wszystkie elementy z listy'''
        self.list.clear()

    def copy(self):
        '''Zwraca kopię listy'''
        return self.list.copy()
    
    def count(self, value):
        '''Zwraca liczbę wystąpień elementu w liście'''
        return self.list.count(value)

    def extend(self, values):
        '''Dodaje wiele elementów do listy'''
        self.list.extend(values)
        self.list.sort()

    def index(self, value):
        '''Zwraca indeks pierwszego wystąpienia elementu w liście'''
        return self.list.index(value)

    def insert(self, index, value):
        '''Wstawia element na podanym indeksie'''
        self.list.insert(index, value)
        self.list.sort()

    def pop(self, index=-1):
        '''Usuwa i zwraca element na podanym indeksie (domyślnie ostatnim)'''
        return self.list.pop(index)

    def remove(self, value):
        '''Usuwa pierwszy wystąpienie elementu z listy'''
        self.list.remove(value)
        self.list.sort()

    def reverse(self):
        '''Odwraca kolejność - tworzy listę posortowaną malejąco'''
        self.list.reverse()
    
sl = SortedList()

for arg in sys.argv[1:]:
    sl.append(float(arg))

print(f'Lista rosnąco: {sl.list}')

sl.reverse()
print(f'Lista malejąco: {sl.list}')