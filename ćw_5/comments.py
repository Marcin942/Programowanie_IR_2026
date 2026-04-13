import sys

comment_sign = sys.argv[1]
filename1 = sys.argv[2]
filename2 = sys.argv[3]

f2 = open(filename2, "w") # "w" oznacza że otwieramy w trybie zapisu

with open(filename1) as f1:
    for line in f1:
        if line[0] != comment_sign:
            f2.write(line)
        else:
            continue
print('Komentarze usunięte')