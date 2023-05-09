#!/usr/bin/python3

for a in range(97, 123):
    a = chr(a)
    if a == 'q' or a == 'e':
        continue
    print(f"{a}", end="".format(a))
