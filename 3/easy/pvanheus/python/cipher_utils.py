def get_offset(c):
    # uses Python inline if: http://stackoverflow.com/questions/11880430/how-to-write-inline-if-statement-for-print
    return 65 if c.isupper() else 97
    
def encrypt_char(c, key):
    offset = get_offset(c)
    return chr(((ord(c) - offset + key) % 26) + offset)

def decrypt_char(c, key):
    offset = get_offset(c)
    ordinal = ord(c) - offset - key + 26 if ((ord(c) - offset) < key) else (ord(c) - offset - key)
    return chr((ordinal % 26) + offset)
