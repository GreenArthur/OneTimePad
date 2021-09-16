
#you need to add the encoding parameter at all times
#it will spit out nonsense if you don't
with open('secretMessage.txt','r',encoding='utf-8') as sm:
    mesg_content = sm.read()

with open('pad.txt','r',encoding='utf-8') as pad:
    pad_content = pad.read()

"""
HOW THIS WORKS 
    similar to encrypting, but instead of the message we feed it the cipher text
    and the pad that used was for encrypting
"""
def decrypt(message,pad):
    plaintext = ""
    for i,j in zip(message,pad):
        xored_value = ord(i) ^ ord(j)
        plaintextvalue = chr(xored_value)
        plaintext +=(plaintextvalue)
    return plaintext

message = decrypt(mesg_content,pad_content)
with open('TheMessage','w+',encoding='utf-8') as TheMessage:
    TheMessage.write(message)