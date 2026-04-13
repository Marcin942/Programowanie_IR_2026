import sys

filename = sys.argv[1]
sum = 0

with open(filename) as f:
    for line in f:
        str_list = line.split(' ')
        price = float(str_list[-1])
        sum += price

print('Kwota do zapłaty: ', sum)