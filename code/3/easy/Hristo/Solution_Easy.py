def alphaIndex(letter):
    return "abcdefghijklmnopqrstuvwxqz".index(letter.lower())

def giveNewLetter(a,b): ##This function gives the new letter based on the code and text
    indexSum = (alphaIndex(a) + alphaIndex(b))
    revAlpha = dict(zip(range(26),"abcdefghijklmnopqrstuvwxqz"))
    if(indexSum > 25):
        indexSum = indexSum%26
    letter = revAlpha[indexSum]
    return letter
    

def cipher(message,code): 
    cipherMessage = ""
    n=0
    
    for i in message:
        try: ##The giveNewLetter only takes in letters as input, all numbers, etc throw errors
            cipherMessage = cipherMessage + giveNewLetter(i,code[n])
            if(n==len(code)-1):
                n=0
            else:
                n+=1
        except(ValueError,TypeError): ##when an error is thrown, the input is added here instead
            cipherMessage = cipherMessage + i
    return cipherMessage


print(cipher("ATTACK AT DAWN!","LEMON")) ##Gives same output as wikipedia example. Works for other examples
