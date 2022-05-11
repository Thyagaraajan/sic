import random

def is_prime(p):
    if p <= 1:
        return False
    for i in range(2, int(p**0.5)+1, 1):
        # print(i)
        if p % i == 0:
            return False
    return True

def generate_prime(n):
    p = random.randrange(2**(n-1)+1, 2**n + 1)
    while True:
        if is_prime(p):
            break
        p = random.randrange(2**(n-1)+1, 2**n + 1)
    return p


def encrypt(p):
    return p**e%n

def decrypt(c,d):
    return c**d%n



p = generate_prime(10)
q = generate_prime(10)
print('p =', p, '\nq =', q)

n = p * q

phi_n = (p-1) * (q-1)

e = random.randrange(2, phi_n)

d = None

print('phi(n) = ', phi_n)
while e % (p-1) == 0 or e % (q-1) == 0 or d == None:
    e = random.randrange(2, phi_n)
    try:
        d = pow(e, -1, phi_n)
    except ValueError:
        continue
    
print('e = ', e, '\nd = ', d)



rand_num = random.randrange(0,1000)
C = encrypt(rand_num)
P = decrypt(C, d)

print("Ciphertext:", C)
print("Plaintext:", P)

if P==rand_num:
    print("VERIFIED")
else:
    print("INCORRECT")