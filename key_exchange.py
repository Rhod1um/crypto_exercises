import math

# diffie-helmann key agreement/exchange protocol

# Alice vælger random element a fra et set N={1,2,3,p-1}=Zp.
# så Zp er {1 - 22}

# value fra 1-22 for alice og for bob (?)

a = 5
b = 6
g = 5
p = 23 # (p er prime)

# A=g^a mod p 

A = (g**a) % p

B = (g**b) % p

print("A:", A, ",", "B:", B)

# k=A^b mod p    k=B^a mod p

k = A**b % p

print(k)

k = B**a % p

print(k)

# k=g^.ab mod p   k er key, den som de deler og er ens for begge

k = g**(a*b) % p

print(k)

k = pow(g,a*b) % p

print(k)

# med noget efter nr. 2 komma er modulus:
k = pow(g,a*b, p)

print(k)