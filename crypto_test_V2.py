def encrypt(key, string):
    encoded = ''
    for i in range(len(string)):
        key_c = ord(key[i % len(key)])
        string_c = ord(string[i % len(string)])
        encoded += chr((key_c + string_c) % 127)
    return encoded


def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)

def main():

    msg = "hello world"
    
    key = "makis"
    msg_crypto = encrypt(key,msg)
    msg_decrypt = decrypt(key,msg_crypto)
    
    print "Message: " , msg
    print "Key : " , key
    print "Encrypted message: " , msg_crypto
    print "Decrypted message: " , msg_decrypt
    makis = ''
    for i in range(len(msg)):
        makis = makis +chr( ord(msg[i]))
    print makis
    


main()
