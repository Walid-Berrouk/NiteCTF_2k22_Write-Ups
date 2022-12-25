import gmpy2
import numpy as np

fn = open("firstnames.py", 'r')
ln = open("lastnames.py", 'r')
fp = open ("primes.py", 'r')
fn_content = fn.readlines()
ln_content = ln.readlines()
prime_arr = fp.readlines()

class RNG:
    def __init__ (self, seed, a, b, p):
        self.seed = seed
        self.a = a
        self.b = b
        self.p = p

    def gen(self):
        out = self.seed
        while True:
            out = (self.a * out + self.b) % self.p
            self.a += 1
            self.b += 1
            self.p += 1
            yield out



name1= input('name1: ').split(' ')
a=fn_content.index(name1[0].strip()+'\n')
b=ln_content.index(name1[1]+'\n')
p=1300
a=a+1
b=b+1
p=p+1

name2= input('name2: ').split(' ')
out =fn_content.index(name2[0]+'\n')
lcg = RNG(out,a,b,p)
gen=lcg.gen()
print(ln_content[next(gen)])
out=next(gen)

print(f"winner = {out} , {out%2}")

for i in range(9):
    for j in range(5):
        out=next(gen)    
    print(f"winner = {out} , {out%2}")
    
def getPrime ():
    prime = int(prime_arr[next(gen)].strip())
    return prime
    
def generate_keys():
    p = getPrime()
    q = getPrime()
    n = p*q
    g = n+1
    l = (p-1)*(q-1)
    mu = gmpy2.invert(((p-1)*(q-1)), n)
    return n, g, l, mu ,p,q


def decrypt2(n, m, g, cipher, rand):
    n_sqr = n * n
    trash = pow(rand, n, n_sqr)
    trash = gmpy2.invert(trash, n_sqr)
    norm = (cipher * trash) % n_sqr
    return ((norm - 1) // n) // ((g-1)// n)




n, g, l, mu,p,q=generate_keys()
rand=next(gen)
lam = int(np.lcm(p - 1, q - 1))
print(f"({n}, {g}, {l}, {mu},{p},{q})\n\n")
cipher=int(input('ciphertext: '))
print(decrypt2(n,mu,g,cipher,rand))