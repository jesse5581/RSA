x = 1 
while x == 1:
    print ('would you like to encrypt, decrypt, or exit?')
    answer = input('?: ')
    if answer == 'exit' or answer == 'Exit':
        print ('Goodbye')
        x = 2
    if answer == 'encrypt' or answer == 'Encrypt':
      encrypt()
    if answer == 'decrypt' or answer == 'Decrypt':
        print ('What would you like to decrypt?')
def encrypt():
  e = input('Please enter an e value:')
  n = input('Please enter an n value:')
  
  
  
  