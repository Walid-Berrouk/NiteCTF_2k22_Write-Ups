#! /usr/bin/python3

from Crypto.Util.number import *
import gmpy2



fp = open (r"primes.py", 'r')
prime_arr = fp.readlines()

# print(len(prime_arr))
flag = b'niteCTF{this_is_a_test_flag}'

def getPrime ():
    prime = int(prime_arr[2000].strip())
    return prime

def generate_keys():
    p = getPrime()
    q = getPrime()
    n = p*q
    g = n+1
    # l is actually the lcm since p-1 and q-1 are primte between them
    l = (p-1)*(q-1)
    mu = gmpy2.invert(((p-1)*(q-1)), n)
    return (n, g, l, mu)

def pallier_encrypt(key, msg, rand):
    n_sqr = key[0]**2
    return (pow(key[1], msg, n_sqr)*pow(rand, key[0], n_sqr) ) % n_sqr

# We Don't need the L function since it isn't applied of the mu in the first place
# def L(key, x) :
#     n = key[0]
#     return (x - 1) // n

def pallier_decrypt(key, cipher) :
    n = key[0]
    n_sqr = key[0]**2
    l = key[2]
    mu = key[3]
    return (pow(cipher, l, n_sqr)*mu) % n

# 
# (L(key, pow(cipher, l, n_sqr))*mu) % n

key=generate_keys()

# Code and come back
# int_flag = int.from_bytes(flag, "big")
# print(b'niteCTF' in int.to_bytes(int_flag, len(flag) + 50,"big"))
# Output : True


flag_encrypted = pallier_encrypt(key, int.from_bytes(flag, "big"), 500)

print(flag_encrypted)
print()


print(int.to_bytes(int(pallier_decrypt(key, flag_encrypted)), 100,"big") )
