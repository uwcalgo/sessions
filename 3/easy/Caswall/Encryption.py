#!/usr/bin/python3
def encrypt(key,text):
	temp = ""
	i,j = 0,0
	while(i < len(text)):
		if(ord(text[i]) > 96 and ord(text[i]) < 123):
			k = j%len(key)
			newchr = ((ord(key[k])-96) + ord(text[i])-97)%26
			temp+= chr(newchr+97)
			j+=1
			i+=1
		else:
			temp+=text[i]
			i+=1
	return temp

def decrypt(key,text):
	temp = ""
	i,j = 0,0
	while(i < len(text)):
		if(ord(text[i]) > 96 and ord(text[i]) < 123):
			k = j%len(key)
			newchr = (ord(text[i]) - (ord(key[k])-96)-97)%26
			temp+= chr(newchr+97)
			j+=1
			i+=1
		else:
			temp+=text[i]
			i+=1
	return temp

key = "fribbit"
encryption = encrypt(key,"the zombies are coming.")
print("Encrypted text:",encryption)
print("Decrpyted text:",decrypt(key,encryption))
