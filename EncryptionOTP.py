import random
import string


with open('message.txt','r') as mesg:
    mesg_content = mesg.read()

#generate a random set of characters base on the length of the message
#and use it as the key 
def Thepad(message):
    pad = ''.join(random.choice(string.printable) for i in range(len(message)))
    return pad
    
"""
HOW THIS WORKS:
    1.for each letter of the message and the pad, we convert it to numbers.
    2.then we xor them.
    3.then we convert them back to characters
Requirements:
    The pads is the most important:
        it must be randomly generated to make it secure 
        it must be at the same length as the message
        Do not reuse the same pad everytime
"""
def encrypt(message, pad):
    ciphertext = ""
    for i, j in zip(message, pad):
        xored_value = ord(i) ^ ord(j)
        ciphervalue = chr(xored_value)
        ciphertext += (ciphervalue)
    return ciphertext



pad = Thepad(mesg_content)
secretMessage = encrypt(mesg_content,pad)


#we write the cipher text and the pad to a text file

#need the "encoding" parameter for windows, not exactly sure why but gives me an error
#if its not there
with open('secretMessage.txt','w+',encoding='utf-8') as ciphertext:
    ciphertext.write(secretMessage)

with open('pad.txt','w+',encoding='utf-8') as thepad:
    thepad.write(pad)



