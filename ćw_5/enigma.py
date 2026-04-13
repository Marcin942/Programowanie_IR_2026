import sys

'''
Operator ^ wykonuje operację bitowego XOR na dwóch liczbach całkowitych.
XOR działa na poziomie bitów (tzn. zer i jedynek w reprezentacji binarnej liczb):
Dla każdego bitu w liczbach wejściowych, wynik jest 1, jeśli bity są różne, 0, jeśli bity są takie same.

Operacja XOR jest symetryczna, co oznacza, że:

Jeśli zaszyfrujesz dane za pomocą klucza, możesz je odszyfrować, wykonując XOR z tym samym kluczem.
(A ^ B) ^ B = A

Przykład:
Oryginalny znak: 'N' (kod ASCII: 78)
Klucz: 7
Szyfrowanie: 78 ^ 7 = 73
Deszyfrowanie: 73 ^ 7 = 78 (co odpowiada 'N').
'''

def encryption(line, key):
    encrypted = []
    for char in line:
        encrypted.append(str(ord(char) ^ key)) # ord(char)^key to operacja XOR pomiędzy kodem ASCII znaku char a kluczem
    return ' '.join(encrypted)

def decryption(line, key):
    decrypted = []
    for num in line.split(): #split dzieli linię na pojedyncze liczby
        decrypted.append(chr(int(num) ^ key)) # int(num)^key to operacja XOR pomiędzy liczbą num a kluczem
                                            # chr() zamienia liczbę na odpowiadający jej znak ASCII
    return ''.join(decrypted)

operation_type = sys.argv[1] 
key = int(sys.argv[2])
filename1 = sys.argv[3]
filename2 = sys.argv[4]

f1 = open(filename1, "r") # "r" oznacza że otwieramy w trybie odczytu
f2 = open(filename2, "w") # "w" oznacza że otwieramy w trybie zapisu

text = f1.read() # read() odczytuje cały plik

if operation_type == '-e':
    f2.write(encryption(text, key))
elif operation_type == '-d':
    f2.write(decryption(text, key))
else:
    print('Pierwszym argumentem musi być -d lub -e')

