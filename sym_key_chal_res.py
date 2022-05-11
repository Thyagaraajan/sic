n = 5

def encrypt(word,n):
    result = ""
    for s in word:
        result += chr((ord(s) + n - 97) % 26 + 97)
    return result

def decrypt(cipher,n):
    res = ""
    for s in cipher:
        res+= chr((ord(s) - n - 97) % 26 + 97)
    return res

word = input("send random word bob : ")
cipher = encrypt(word, n)
print("CIPHERTEXT:", cipher)
print("DECRYPTED:", decrypt(cipher, n))
if word == decrypt(cipher, n):
    print("GOOD")
else:
    print("BAD")