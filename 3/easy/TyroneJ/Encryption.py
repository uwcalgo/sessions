def v_square(a):
        v_grid = []
        
        for i in range(26):
                prefix = ""
                for j in range(i):
                        prefix = prefix + a[j]
                v_grid.append(a[i:] + prefix)
        return v_grid
             
def key_word(k,txt):
        if(len(k) == len(txt)):
                return k
        while(len(k) < len(txt)):
                for i in range(len(k)):
                        if(len(k) == len(txt)):
                                break
                        prefix = ""
                        for j in range(i +1):
                                prefix = k[j]
                        k = k + prefix
        return k

def remove(txt,alpha):
        txt2 = ""
        other = []
        num_other = []
        for i in range(len(txt)):
                if(txt[i] in alpha):
                        txt2 = txt2 + txt[i]
                else:
                        other.append(txt[i])
        return [txt2, other]


def encrypt(k,txt,b):
        encryption = ""
        txt2 = remove(txt,b)[0]
        other_chars = remove(txt,b)[1]
        key = key_word(k,txt2)
        v_table = v_square(b)
        row_key = b
        for x in range(len(key)):
                index1 = row_key.index(key[x])
                index2 = row_key.index(txt2[x])
                encryption = encryption + v_table[index1][index2]
        
        if(len(other_chars) == 0):
                return encryption
        x = 0
        
        z = 0
        encr = ""
        while(x < len(txt) and z <= len(encryption)):
                count = 0
                for y in range(len(other_chars)):      
                        if(txt[x] == other_chars[y]):
                                encr = encr +(txt[x])
                                count = 1
                                break
                if(count != 1):
                        encr = encr + (encryption[z])
                        z += 1
                x += 1
                        
        return encr

def decrypt(k,txt,b):
        txt2 = remove(txt,b)[0]
        other_chars = remove(txt,b)[1]
        key = key_word(k,txt2)
        v_table = v_square(b)
        row = b
        decryption = ""
        for x in range (len(key)):
                index1 = row.index(key[x])
                row2 = v_table[index1]
                plain_text = row[row2.index(txt2[x])]
                decryption = decryption + plain_text
        if(len(other_chars) == 0):
                return decryption
        x = 0
        
        z = 0
        decr = ""
        while(x < len(txt) and z <= len(decryption)):
                count = 0
                for y in range(len(other_chars)):      
                        if(txt[x] == other_chars[y]):
                                decr = decr +(txt[x])
                                count = 1
                                break
                if(count != 1):
                        decr = decr + (decryption[z])
                        z += 1
                x += 1
        return decr
        
        
import string
alph = string.ascii_uppercase
op = "1"
while(op == "1" or op == "2"):
        op = input("Welcome to the encryption centre. Please select an option via numeric keys. eg. 1 for 1)\n1) Encrypt a message.\n2) Decrypt a message.\nq) to quit the program \n\n: ")
        if(op == str(1)):
                keyW = input("Please enter the key: ")
                keyW = keyW.upper()
                msg = input("please enter the message to be encrypted: ")
                msg = msg.upper()
                print(encrypt(keyW,msg,alph))
        if(op == str(2)):
                keyW = input("Please enter the key: ")
                keyW = keyW.upper()
                encrypted = input("please enter the message to be decrypted: ")
                encrypted = encrypted.upper()
                print(decrypt(keyW,encrypted,alph))
        


        


    
