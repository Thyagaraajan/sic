import random

def RSA_sig(M):
    S = M**d % n
    return S

def RSA_ver(S):
    M_1 = S**e % n
    return M_1

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

rand_num = random.randrange(0,500)
print("MESSAGE:", rand_num)
S = RSA_sig(rand_num)
print("AFTER SIGNING:", S)
M = RSA_ver(S)
print("VERFIED MESSAGE:", M)
if rand_num == M:
    print("VERIFIED")
else:
    print("INVALID")    
