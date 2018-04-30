# -*- coding: utf-8 -*-
import time
start = time.time()

n = 21971
e = 131
d = 17867

message = "Hello World"
encrypted_message = ''
decrypted_message = ''
###########Encryption##########
for x in message:
    numerize = ord(x)
    encrypt = pow(numerize, e, n)
    denumerize = unichr(encrypt)
    encrypted_message += denumerize
    
print encrypted_message

##########Decyption##########
for t in encrypted_message:
    numerize = ord(t)
    decrypt = pow(numerize, d, n)
    demunerize = chr(decrypt)
    decrypted_message += denumerize

print decrypted_message

end = time.time()
print(end - start)

start = time.time()

encrypted_message2 = ''
decrypted_message2 = ''
LUT_encryption = dict()
LUT_decryption = dict()

##########eNCRYPTION V2##########

for x in message:
    if x in LUT_encryption:
            encrypted_message2 += LUT_encryption[x]
    else:
        numerize = ord(x)
        encrypt = pow(numerize, e, n)
        denumerize = unichr(encrypt)
        encrypted_message2 += denumerize
        LUT_encryption[x] = denumerize
    
print encrypted_message2

##########eNCRYPTION V2##########

for t in encrypted_message2:
    if t in LUT_encryption:
            decrypted_message2 += LUT_decryption[x]
    else:
        numerize = ord(t)
        encrypt = pow(numerize, e, n)
        denumerize = unichr(decrypt)
        encrypted_message2 += denumerize
        LUT_decryption[x] = denumerize
    
print encrypted_message2

end = time.time()
print(end - start)

© 2018 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
API
Training
Shop
Blog
About
