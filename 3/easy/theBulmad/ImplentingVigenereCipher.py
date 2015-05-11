#Implementing the Vigenere Cipher
#Bulmad
#2015-05-09

#pt = plaintext
#k  = key
#ct = ciphertext
#key_exp = key expanding to the length of pt
    
def encrypt(pt,k):
    
    alpha_rotor = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ct = ""
    key_exp = ""

    #expanding the key so that it can be plaintext length
    i = 0
    r = 0
    while(i < len(pt)):
        key_exp = key_exp + k[r]
        if(r == len(k) - 1):
            r = 0
        else:
            r = r + 1
        i = i + 1
    #generating the cipheredtext
    j = 0
    while(j < len(pt)):
        letter = alpha_rotor.find(pt[j].upper()) + alpha_rotor.find(key_exp[j].upper())
        if(letter > 25):
            letter = letter - 26
        else:
            pass
        ct = ct + alpha_rotor[letter]
        j = j + 1
    return ct
def decrypt(ct,k):
    alpha_rotor = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pt = ""
    key_exp = ""

    #expanding the key so that it can be plaintext length
    i = 0
    r = 0
    while(i < len(ct)):
        key_exp = key_exp + k[r]
        if(r == len(k) - 1):
            r = 0
        else:
            r = r + 1
        i = i + 1
    #generating the cipheredtext
    j = 0
    while(j < len(ct)):
        letter = alpha_rotor.find(ct[j].upper()) - alpha_rotor.find(key_exp[j].upper())
        if(letter < 0):
            letter = letter + 26
        else:
            pass
        pt = pt + alpha_rotor[letter]
        j = j + 1
    return pt
plaintext = input("Plaintext : ")
key = input("Key : ")
print(encrypt(plaintext,key))
cryptedtext = input("Cryptedtext : ")
key = input("Key : ")
print(decrypt(cryptedtext,key))

            
              
