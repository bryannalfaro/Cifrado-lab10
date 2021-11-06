from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
import hashlib
import random

def EncryptCBC(data, key):
    b = random.randint(2,key[2]-1) # usa el mismo primo p que las claves generadas
    u = pow(key[0],b) #g^b
    v = pow(key[1],b,key[2]-1) # g^(a*b)modp-1 <- h^(b) mod p-1

    key = (u+v)
    sharedkey = str(key)
    plainText =  sharedkey.encode('utf-8')
    hashKey = hashlib.sha256(plainText).digest()

    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(hashKey, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    ct = b64encode(iv+ct_bytes).decode('utf-8')
    result = ct
    return u,result

def DecryptCBC(result,a,u,p):
    v = pow(u,a,p-1) # g^(b*a)modp-1 <- u^(a) mod p-1

    sharedkey = str(u+v)
    plainText =  sharedkey.encode('utf-8')
    hashKey = hashlib.sha256(plainText).digest()

    cipher = AES.new(hashKey, AES.MODE_CBC, b64decode(result)[:AES.block_size])
    pt = unpad(cipher.decrypt(b64decode(result)[AES.block_size:]), AES.block_size)
    return pt.decode('utf-8')