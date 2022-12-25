#! /usr/bin/python3

from Crypto.Util.number import *
import gmpy2



fp = open (r"primes.py", 'r')
prime_arr = fp.readlines()

flag_encrypted = 4342927386430770292737526302064953436148753643610151964740061413150996844272364568908877777496524289178325221065261188459822842088104206254531364659678658339392175752029856204319171553623396322526719744601760837931178243419056264600228691940569400481920580494452796030163010191979526733758095350162950249629661542686521933614490726525981446045532401326968552757982040972277985100627014497306997139181458745650239394880111392244610079839681919377248020187747704096520691696997406156439160823559367821356445469486552475554194949074989873664924041728339859549077861902087392780825054566388122134948510180243502533744117

def getPrime(i):
    prime = int(prime_arr[i].strip())
    return prime

def generate_keys(i_p, i_q):
    p = getPrime(i_p)
    q = getPrime(i_q)
    n = p*q
    g = n+1
    # l is actually the lcm since p-1 and q-1 are primte between them
    l = (p-1)*(q-1)
    mu = gmpy2.invert(((p-1)*(q-1)), n)
    return (n, g, l, mu)


def pallier_decrypt(key, cipher, rand):
    n = key[0]
    n_sqr = key[0]**2
    g = key[1]
    trash = pow(rand, n, n_sqr)
    trash = gmpy2.invert(trash, n_sqr)
    norm = (cipher * trash) % n_sqr
    return ((norm - 1) // n) // ((g-1)// n)




for i_p in range(0, len(prime_arr)) :
    print("Testing prime number : " + str(i_p))
    for i_q in range(0, len(prime_arr)) : 
        print("Testing sub prime number : " + str(i_q))
        key = generate_keys(i_p,i_q)
        n = key[0]
        for rand in range(1, n) :
            flag = int.to_bytes(int(pallier_decrypt(key, flag_encrypted, rand)), 200,"big")
            if b'niteCTF' in flag :
                print(flag)