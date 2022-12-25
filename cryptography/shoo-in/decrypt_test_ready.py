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


def pallier_decrypt(key, cipher, rand):
    n = key[0]
    n_sqr = key[0]**2
    g = key[1]
    trash = pow(rand, n, n_sqr)
    trash = gmpy2.invert(trash, n_sqr)
    norm = (cipher * trash) % n_sqr
    return ((norm - 1) // n) // ((g-1)// n)


key=generate_keys()


flag_encrypted = pallier_encrypt(key, int.from_bytes(flag, "big"), 500)

print(flag_encrypted)
print()


print(int.to_bytes(int(pallier_decrypt(key, flag_encrypted, 500)), 100,"big") )

# Output :
# 7694427615840443130858096373401224558539903044741575702943728598414632303408266624324011219355205559444427676560477583014965750895294785985389081885050566052332498291576569153874802085716149381515601370106320893204524724116014166179255914615238597107940946306361523717921498438303922836331203076890613966312161659438448337178431128381275248116714699350171090450421388648440774490993334126364946497882716632517555084480916443347050755395299322517272850724094929471549986684154556382181955039816674499552518749757812045265071783969431974173440655121041145014688051186459143624609700307362817236197938999101205973450287

# b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00niteCTF{this_is_a_test_flag}'