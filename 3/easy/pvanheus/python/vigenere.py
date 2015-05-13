#!/usr/bin/env python

from __future__ import print_function
from cipher_utils import encrypt_char, decrypt_char, get_offset

def to_nums(key):
    nums = []
    for letter in key:
        num = ord(letter) - get_offset(letter)
        nums.append(num)
    return nums

def vigenere_imperative(message, key, encrypt=True):
    result = ''
    key_index = 0
    key = to_nums(key)
    for c in message:
        if not c.isalpha():
            result += c
        else:
            if encrypt:
                result += encrypt_char(c, key[key_index])
            else:
                result += decrypt_char(c, key[key_index])
            key_index = (key_index + 1) % len(key)
    return result


def vigenere_functional(message, key, encrypt=True):
    op = encrypt_char if encrypt else decrypt_char
    key = [ord(c) - get_offset(c) for c in key]

    def vigenere_helper(message, key_index, ciphertext, op):
        return ciphertext if message == '' else vigenere_helper(message[1:], 
            (((key_index + 1) % len(key)) if message[0].isalpha() else key_index), 
                    ciphertext + (op(message[0], key[key_index]) if message[0].isalpha() else message[0]), op)

    return vigenere_helper(message, 0, '', op)

if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Implement Vigenere cipher")
    parser.add_argument('-t', '--test', default=False, 
        action='store_true', help='Run on test dataset')
    parser.add_argument('-f', '--functional', default=False, 
        action='store_true', help='Use functional implementation of algorithm')
    args = parser.parse_args()

    if args.functional:
        vigenere = vigenere_functional
    else:
        vigenere = vigenere_imperative

    if args.test:
        message = 'ATTACK AT DAWN'
        key = 'LEMON'
        count = 0
        for vigenere in (vigenere_imperative, vigenere_functional):
            count += 1
            encrypted = vigenere(message, key)
            decrypted = vigenere(encrypted, key, encrypt=False)
            assert decrypted == message, "Algorithm failed, expected {} got {}".format(message, decrypted)
            print("Test {} passed: message {} key {} ciphertext {}".format(count, message, key, encrypted))
    else:
        message = sys.stdin.next().rstrip()
        key = sys.stdin.next().rstrip()
        print(vigenere(message, key))
