import random

def elgamal_sign(M):
    r = random.randrange(2, p-1)
    while True:
        try:
            r_1 = pow(r, -1, p-1)
            break
        except:
            r = random.randrange(2, p-1)
    S1 = e1**r % p
    S2 = ((M - d*S1)*r_1) % (p-1)
    return M, S1, S2

def elgammal_verify(M, S1, S2):
    V1 = e1**M % p
    V2 = (e2**S1) * (S1**S2) % p
    print(V1, V2)
    if V1 == V2:
        return "Verification True"
    return "Verification False"

def gcd(a, b):
	if (a == 0):
		return b;
	return gcd(b % a, a);
        
def generators(n):
    while(True):
        a = random.randint(2, n-1) 
        if((n-1)%a != 1):
            return a

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
e1 = generators(p)
M = 120
d = random.randrange(2, p-1)
e2 = e1**d % p
print('Public key : ', e1, e2, p)
print('Private key : ', d)

M, S1, S2 = elgamal_sign(M)
print("M S1 S2 = ", M, S1, S2)
print(elgammal_verify(M, S1, S2))