def decrypt(d,n2):
    encrypted_message = ''
    decrypted_message = ''
    
def encrypt(e,n):
  encrypted_message = ''
  decrypted_message = ''
  message = input('What would you like to encrypt?: ')
  for x in message:
    numerize = ord(x)
    encrypt1 = pow(numerize, e, n)
    denumerize = chr(encrypt1)
    encrypted_message += denumerize
  print (encrypted_message)
xx = 1 
while xx == 1:
    print ('would you like to encrypt, decrypt, or exit?')
    answer = input('?: ')
    if answer == 'exit' or answer == 'Exit':
        print ('Goodbye')
        xx = 2
    if answer == 'encrypt' or answer == 'Encrypt':
      e = int(input('Please enter an e value:'))
      n = int(input('Please enter an n value:'))
      encrypt(e,n)
    if answer == 'decrypt' or answer == 'Decrypt':
         d = int(input('Please enter a d value:'))
         n2 = int(input('Please enter an n2 value:'))
