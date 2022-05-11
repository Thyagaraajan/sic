import random

def RSA_Sign(M):
    return M**d % n, M

def RSA_verify(M, S):
    M_1 = S**e % n
    if M == M_1:
        return "Valid Signature"
    return "Signature does not match"
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

M = 120
S, M = RSA_Sign(M)
print('Signature : ', S)

print('Verify ? ', RSA_verify(M, S))