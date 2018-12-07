import io


##file = io.open("files/messageGreek.txt","r",encoding="utf-8")
file = io.open("files/messageGreek.txt","rb+")
msg = file.read()
file.close()
print msg

ASCII_code = []

for i in range(len(msg)):
    ASCII_code.append(ord(msg[i]))

ASCII_char = []
for i in range(len(ASCII_code)):
    ASCII_char.append(unichr(ASCII_code[i]).encode('utf-8'))


##file = open("files/messageToGreek.txt","wb+")
##file.write(msg)
##file.close()


print msg
print ASCII_code
print ASCII_char


print "ti fasi ? "
b = msg[4]
makis = ord(b)
sakis = unichr(makis).encode('utf-8')
print b,makis,sakis
