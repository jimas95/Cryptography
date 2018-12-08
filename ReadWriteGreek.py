# -*- coding: utf-8 -*-

import io


file = io.open("files/messageGreek.txt","r",encoding="utf-8")
##file = open("files/messageGreek.txt","rb+")
msg = file.read()
file.close()

ASCII_code = []
ASCII_char = []


for i in range(len(msg)):
    ASCII_code.append(ord(msg[i]))

for i in range(len(ASCII_code)):
    ASCII_char.append(unichr(ASCII_code[i]))


text = ''.join(ASCII_char)
file = open("files/messageToGreek.txt","w")
file.write(text.encode('utf-8'))
file.close()


print msg
print ASCII_code
print ASCII_char
print "TEXT \n" ,text


print "ti fasi ? "
b = msg[4]
makis = ord(b)
sakis = unichr(makis)
print b,makis,sakis
