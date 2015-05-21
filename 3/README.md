# Session 3 ### 13 May 2015


Discussed languages
===================
## Python

### functions

#### [ord](https://docs.python.org/2/library/functions.html#ord) 

``` >>> ord('r')```
```114```

#### [chr](https://docs.python.org/2/library/functions.html#chr)

 ```>>> chr(114)```
```'r'```
		
Problems
========

### String encryption

*String encryption*: Letter substitution ciphers work by mapping each letter of the alphabet to another letter in some predictable way. A simple example is the [Caesar cipher](http://en.wikipedia.org/wiki/Caesar_cipher) where a fixed offset is used to choose the substitution letter. For example the offset 13 turns **a** into **n**, **b** into **o**, and so on. The cipher wraps around the alphabet, so for example **n** becomes **a**. A more sophisticated cipher is the [Vigenère cipher](http://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) where the key is a sequence of offsets, normally represented as a word. For example **baa** stands for the offsets **2 1 1**. These are then repeated until the entire text is encrypted. The challenge here is to implement functions to encrypt and decrypt with the Vigenère cipher. Non-letter characters (e.g. whitespace and punctuation) should be ignored. For example, given the key **fribbit** and the text **the zombies are coming**, you should get the encrypted text (ciphertext) **zzn bqvvowb ctn wuerpi**.

### [Marching band](http://www.olympiad.org.za/olympiad/wp-content/uploads/2013/01/SBITC-Heats-Problems-v-13-04-14-Final.pdf) (M)

Rated medium, this is problem 3 from the [2013 Standard Bank IT Challenge heats](http://www.olympiad.org.za/olympiad/wp-content/uploads/2013/01/SBITC-Heats-Problems-v-13-04-14-Final.pdf).

###	[Crowd Control](http://www.olympiad.org.za/olympiad/wp-content/uploads/2014/09/2014-SBITC-Complete-problem-set.pdf) (H)

Rated hard, this is problem 2 from the [SBITC 2014 problem set](http://www.olympiad.org.za/olympiad/wp-content/uploads/2014/09/2014-SBITC-Complete-problem-set.pdf).
	
Take home problem
=================

