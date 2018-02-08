import encoder




def get_key():
    with open('creds.str', 'r') as fp:
        encoded = fp.read()
    return encoder.decode(encoded, input('Password For Creds?\n'))

def write_key(key):
    encoded = encoder.encode(key, input('password to store?\n'))
    with open('creds.str', 'w') as fp:
        fp.write(encoded)
        
key = get_key()