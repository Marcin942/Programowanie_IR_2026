import sys

def TextCalc(line):
    str_list = line.split(' ')
    x1 = float(str_list[0])
    operator = str_list[1]
    x2 = float(str_list[2])
    if operator == '+':
        result = x1 + x2
    elif operator == '-':
        result = x1 - x2
    elif operator == '*':
        result = x1 * x2
    elif operator == '/':
        result = x1 / x2
    elif operator == '%':
        result = x1 % x2
    elif operator == '^':
        result = x1 ** x2
    return result


filename1 = sys.argv[1]
filename2 = sys.argv[2]

f2 = open(filename2, "w") # "w" oznacza że otwieramy w trybie zapisu

with open(filename1) as f1:
    for line in f1:
        result = TextCalc(line)
        f2.write(line.strip() + ' = ' + str(result) + '\n') 
         # line.strip() usuwa tzw. "białe znaki" z początku i końca linii
         # "białe znaki" to spacje, tabulatory, znaki nowej linii - w tym przypadku chcemy usunąć znak nowej linii
        

