import random
import json
import pprint
import time


def decrypt(F, d):
    if d == 0:
        return 1
    if d == 1:
        return F
    w, r = divmod(d, 2)
    if r == 1:
        return decrypt(F * F % n, w) * F % n
    else:
        return decrypt(F * F % n, w)


def correct():
    for i in range(len(C)):
        if len(str(P[i])) % 2 != 0:
            y = str(0) + str(P[i])
            P.remove(str(P[i]))
            P.insert(i, y)


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


def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
          "r", "s", "t", "u", "v", "w", "x", "y", "z", ",", ".", "!", "?", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
          "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "{", "}", ":", '"', "α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "ι", "κ", "λ", "μ", "ν", "ξ", "ο", "π", "ρ",
          "σ", "τ", "η", "φ", "χ", "ψ", "ω", "ς", "Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ", "Ν", "Ξ", "Ο", "Π", "Ρ",
          "Σ", "Τ", "Η", "Φ", "Χ", "Ψ", "Ω"]

number = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
          "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27",
          "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44",
          "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78",
          "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100", "101", "102", "103",
          "104", "105", "106", "107", "108", "109", "110"]

print('\n')

print (len(letter))
print (len(number))
#print(', '.join(letter))
#print(', '.join(number))

def Decrypt():
    # decrypts an encoded message
    global m, P, C, x, h, p, Text, y, w
    P = []
    C = str(input("Enter ciphertext blocks:"))
    C = C.lstrip('[')
    C = C.rstrip(']')
    C = C.split(',')
    for i in range(len(C)):
        x = decrypt(int(C[i]), d)
        P.append(str(x))
    correct()
    print(P)
    h = len(P[0])
    p = []
    for i in range(len(C)):
        for n in range(int(h / 2)):
            p.append(str(P[i][(2 * n):((2 * n) + 2)]))

    Text = []
    for i in range(len(p)):
        for j in range(len(letter)):
            if str(p[i]) == number[j]:
                Text.append(letter[j])
    PText = str()
    for i in range(len(Text) -1):
        PText = PText + str(Text[i])
    print("Plaintext is:", PText)


def Encrypt():
    # encrypts a plaintext message using the current key
    global plaintext, numP, q, j, z, X, C
    plaintext = (input("Enter Plaintext :"))
   # plaintext = plaintext.lower()
    numP = []
    for i in range(len(plaintext)):
        for j in range(len(letter)): 
            if plaintext[i] == letter[j]: #ord() -> ASCII CHAR -> int 
                numP.append(number[j])
    h = (len(str(n)) // 2) - 1
    q = len(numP) % h
    print (h)
    print (q)
    #if b > a:
    for i in range(h - q):
        numP.append(number[random.randint(0, 25)])
    j = len(numP) / h
    print(numP)
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
    print("Number of Ciphertext blocks:", len(C)-1)


def setup():
    global n, e, d
    while True:
        try:
            n = int(input(" Enter a value for n :"))
            if n > 2:
                break
        except ValueError:
            print('please enter a number')
    while 1 != 2:
        try:
            e = int(input(" Enter a value for e :"))
            if e >= 2:
                break
        except ValueError:
            print('please enter a number')
    while True:
        try:
            d = int(input(" Enter a value for d. If d unknown, enter 0 :"))
            if d >= 0:
                break
        except ValueError:
            print('please enter a number')




# setup()
n = 2537 # find bigger prime numbers 
e = 13
d = 937

print("To redefine n,e, or d, type 'n','e',... etc.")
print("To encrypt a message with the current key, type 'Encrypt'")
print("To decrypt a message with the current key, type 'Decrypt'")
print("Type quit to exit")
print('\n')
print('\n')

mm = str()
while mm != 'quit':
    mm = input("Enter Command...")
    if mm.lower() == 'encrypt':
        Encrypt()
    elif mm.lower() == 'decrypt':
        Decrypt()
    elif mm.lower() == 'n':
        try:
            print('current n = ', n)
            n = int(input(" Enter a value for n :"))
        except ValueError:
            print('That is not a valid entry')
    elif mm.lower() == 'help':
        print("To redefine n,e, or d, type 'n','e',... etc.")
        print("To encrypt a message with the current key, type 'Encrypt'")
        print("To decrypt a message with the current key, type 'Decrypt'")
        print("Type quit to exit")
        print('\n')
        print('\n')
    elif mm.lower() == 'e':
        try:
            print('current e = ', e)
            e = int(input(" Enter a value for e :"))
        except ValueError:
            print('That is not a valid entry')
    elif mm.lower() == 'd':
        try:
            print('current d = ', d)
            d = int(input(" Enter a value for d :"))
        except ValueError:
            print('That is not a valid entry')
    else:
        if mm != 'quit':
            ii = random.randint(0, 6)
            statements = ["I sorry, Brother. I'm afraid i can't do that", "I'm begging you....read the directions",
                          "Nah ahh ahh, didnt say the magic word", "This input is....UNACCEPTABLE!!",
                          "Seriously....was that even a word???", "Please follow the directions",
                          "Just type 'help' if you are really that lost"]
            print(statements[ii])
