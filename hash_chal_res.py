import time

ts = round(time.time())

def Hash(wor,n):
    result = 0
    wor = str(wor)
    for s in wor:
        result += ((ord(s) + n - 97) % 26 + 97)
    return result

def verify(hash_val,ts):
    if hash_val==Hash(ts,4):
        print("MATCHING")
    else:
        print("NOT MATCHING")
    
print("MESSAGE", ts)
res = Hash(ts,4)
print("HASH", res)
verify(res,ts)