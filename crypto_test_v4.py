import random
import time
n = 2537
e = 13
d = 937

number = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
          "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27",
          "28", "29", "30", "31"]


def Encrypt():
    # encrypts a plaintext message using the current key
    global plaintext, numP, q, j, z, X, C
    plaintext = (input("Enter Plaintext :"))
    plaintext = plaintext.lower()
    numP = []
    for i in range(len(plaintext)):
        numP.append(ord(plaintext[i]))
    h = (len(str(n)) // 2) - 1
    q = len(numP) % h
    for i in range(h - q):
        numP.append(random.randint(0, 127))
    j = len(numP) / h
    # print(numP)
    X = []
    z = 0
    for m in range(h - 1):
        z += 2
    group(j, h, z)
    k = len(X)
    C = []
    for i in range(k):
        b = X[i]
        r = cipher(b, e)
        C.append(r)
    print("Ciphertext:", C)
    print("Number of Ciphertext blocks:", len(C))

def cipher(b, e):
    if e == 0:
        return 1
    if e == 1:
        return b
    w, r = divmod(e, 2)
    if r == 1:
        return cipher(b * b % n, w) * b % n
    else:
        return cipher(b * b % n, w)
    
def group(j, h, z):
    for i in range(int(j)):
        y = 0
        for n in range(h):
            y += int(numP[(h * i) + n]) * (10 ** (z - 2 * n))
        X.append(int(y))
        
def main():
    Encrypt()



main()
