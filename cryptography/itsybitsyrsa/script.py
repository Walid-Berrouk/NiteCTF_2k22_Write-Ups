#! /usr/bin/python3

from Crypto.Util.number import *
from gmpy2 import iroot

# n is too big, not taken in consideration
# fn = open('n_value', 'r')
# n = fn.readline().split("=")[1].strip()


# e value
fe = open('e_value', 'r')
e = int(fe.readline().split("=")[1].strip())

# c value
fc = open('c_value', 'r')
c = int(fc.readline().split("=")[1].strip())


print(iroot(c, 19))

output = long_to_bytes(int(iroot(c, e)[0]))
print(output, end="")
if iroot(c,e)[1] == True : print(" is a true root")
else : print (" is an approximate root")
flag = str(output).strip("b'")
print(flag)