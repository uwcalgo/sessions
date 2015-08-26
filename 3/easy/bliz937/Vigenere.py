# Vigenère cipher

def encrypt(text, key):
    keyLen = len(key)
    
    if(len(text) == 0 or keyLen == 0 or type(text) != str or type(key) != str):
        return "Not a valid key or string"

    arrayKey, keyIndx, encrypted = [abs(ord(i) - 97) for i in key], 0, ""
        
    for i in text:
        i = i.lower()

        if(i not in "abcdefghijklmnopqrstyuvwxyz "):            
            continue
        elif(i == " "):
            encrypted += i
            continue

        e = (abs(ord(i) - 97) + arrayKey[keyIndx]) % 26
        keyIndx += 1

        if(keyIndx == keyLen):
            keyIndx = 0

        encrypted += chr(e + 97)

    return encrypted

def decrypt(text, key):
    keyLen = len(key)
    
    if(len(text) == 0 or keyLen == 0 or type(text) != str or type(key) != str):
        return "Not a valid key or string"

    arrayKey, keyIndx, decrypted = [abs(ord(i) - 97) for i in key], 0, ""
        
    for i in text:
        if(i == " "):
            decrypted += i
            continue

        e = ((ord(i) - 97) - arrayKey[keyIndx]) % 26

        keyIndx += 1

        if(keyIndx == keyLen):
            keyIndx = 0

        decrypted += chr(e + 97)

    return decrypted

if(__name__ == "__main__"):
    text = "the zombies are coming"
    key = "fribbit"

    encrypted = encrypt(text, key)
    print("Encrypted: %s" % encrypted)
    decrypted = decrypt(encrypted, key)
    print("Decrypted: %s" % decrypted)