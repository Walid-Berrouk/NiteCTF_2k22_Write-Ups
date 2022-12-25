# itsybitsyrsa

## Write-Up

When we annalyse the values of rsa, we can see that we have a smaal `e` value with a too big `n` value (surpasses the integer range)

Our main reflex is to try an attack on rsa when the `e` value is too small. Basically, here is how the ciphertext is formed :

<img src="./enc.svg" alt="RSA Encryption" style="background-color: white;"/>

As we can see, and since the `n` value is too big, the mod will basically return the same value. So, to decrypt the message, the only thing to do is to do the `e`th root of the ciphertext.

you can see the code exploit here :

```python
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
```

And here is the output :

```
(mpz(3272916049721142499947688295733093290957148771109821577914942913616526059378599293), True)
b'nitectf{rsa_can_be_very_adaptable}' is a true root
nitectf{rsa_can_be_very_adaptable}
```

## Flag

nitectf{rsa_can_be_very_adaptable}

## More information

https://en.wikipedia.org/wiki/RSA_(cryptosystem)
https://www.johndcook.com/blog/2019/03/06/rsa-exponent-3/