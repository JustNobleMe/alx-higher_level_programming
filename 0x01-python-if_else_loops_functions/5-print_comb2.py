#!/usr/bin/python3

for i in range(0, 99):
    print("{0:0=2d}, ".format(i), end="")
i += 1
print("{:d}".format(i))
