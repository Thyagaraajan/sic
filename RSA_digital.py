
import copy

# Function to find gcd
# of two numbers

def power(m,d,N):
    base = m
    power = d
    n = 1
    for i in range(1,power+1):
        n=(base*n)%N
    
    return n

def euclid(m, n):
	
	if n == 0:
		return m
	else:
		r = m % n
		return euclid(n, r)
	
	
# Program to find
# Multiplicative inverse
def exteuclid(a, b):
	
	r1 = a
	r2 = b
	s1 = int(1)
	s2 = int(0)
	t1 = int(0)
	t2 = int(1)
	
	while r2 > 0:
		
		q = r1//r2
		r = r1-q * r2
		r1 = r2
		r2 = r
		s = s1-q * s2
		s1 = s2
		s2 = s
		t = t1-q * t2
		t1 = t2
		t2 = t
		
	if t1 < 0:
		t1 = t1 % a
		
	return (r1, t1)

def binaryonvert(n):
    temp=[]
    
    while n>0:
        r=n%2
        temp.append(r)
        n=n//2
    
    diff=8-len(temp)
    
    for i in range(0,diff):
        temp.append(0)
    
    temp.reverse()
    return temp

def _32bit(singlelist):
    
    #print(singlelist)
    
    binary_list=[]
    
    for i in range(0,len(singlelist)):
            temp=binaryonvert(singlelist[i])
            for j in range(0,len(temp)):
                binary_list.append(temp[j])

    #print(binary_list)
    return binary_list
        
input1="this is "
list1=[]
temp=[]
coptemp = []

for i in range (0,len(input1)):
    if not(i==0) and i % 4 ==0:
        coptemp = copy.deepcopy(temp)
        list1.append(coptemp)
        temp.clear()
    temp.append(input1[i])

if len(temp)<4:
    for i in range(0,4-len(temp)):
        temp.append(' ')
        
list1.append(temp)

list2=copy.deepcopy(list1)

for i in range(len(list2)):
    for j in range(0,4):
        list2[i][j]=ord(list2[i][j])

#binaryonvert(32)
_2dlist=[]
for i in range(len(list2)):
    _2dlist.append(_32bit(list2[i]))

for i in range(0,len(_2dlist)):
    print(_2dlist[i])
    
msg_digest=[]
for i in range (0,32):
    cnt=0
    cnt1=0
    for j in range(0,len(_2dlist)):
        #print(_2dlist[j][i],end=",")
        if _2dlist[j][i]==0:
            cnt=cnt+1
        elif _2dlist[j][i]==1:
            cnt1=cnt+1
    
    #cnt2=max(cnt1,cnt)
    if cnt%2==0 and cnt1%2==0:
        msg_digest.append(0)
    else:
        msg_digest.append(1)
            
    #print(" ")

print(" ")
print("The hashed msg is ")
print(msg_digest)

p = 823
q = 953
n = p * q
Pn = (p-1)*(q-1)
key = []

for i in range(2, Pn):
	
	gcd = euclid(Pn, i)
	
	if gcd == 1:
		key.append(i)

e = 313

r, d = exteuclid(Pn, e)
if r == 1:
	d = d
	print("decryption key is: ", d)
	
else:
	print("Multiplicative inverse for\
	the given encryption key does not \
	exist. Choose a different encryption key ")


M = 1946439251

S = power(M,d,n)

print(S)

M1 = power(S,e,n)
print(M1)
if (M%n) == M1:
	print("As M = M1, Accept the\
	message sent by Alice")
else:
    
	print("As M not equal to M1,\
	Do not accept the message\
	sent by Alice ")

