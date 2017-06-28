#Caeser Cipher Encryption/Decryption

MAX_KEY_SIZE = 26

def getKey():
    key = int(input('Enter the key value:'))
    if key > MAX_KEY_SIZE:
        print('Key size too big. Please try again.')
        getKey()
    return key

def getPhrase():
    phrase = input('Enter the cipher text:')
    return phrase

def encrypt():
    key = getKey()
    phrase = getPhrase()
    cipher = ""
    for cipherText in phrase:
        cipherVal = ord(cipherText) + key
        if cipherVal > ord('z'):
            cipherVal -= 26
        cipherChar = chr(cipherVal)
        cipher += cipherChar
    print(cipher)

def decrypt():
    key = getKey()
    phrase = getPhrase()
    cipher = ""
    for cipherText in phrase:
        cipherVal = ord(cipherText) - key
        if cipherVal < ord('a'):
            cipherVal += 26
        cipherChar = chr(cipherVal)
        cipher += cipherChar
    print(cipher)

def caeser():
    command = input('Do you wish to (e)ncrypt or (d)ecrypt a cipher?')
    mode = 'A'
    if command == 'd':
        mode = 'd'
        decrypt()
    elif command == 'e':
        mode = 'e'
        encrypt()
    else:
        print('Invalid selection, please try again.')
        caeser()

caeser()