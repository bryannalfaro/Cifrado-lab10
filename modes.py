from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
import hashlib

def binpow(a,b):
    if b==0:
        return 1
    result = binpow(a,b//2)
    if b % 2:
        return result * result *a
    else:
        return result*result

def EncryptCBC(data, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    ct = b64encode(iv+ct_bytes).decode('utf-8')
    result = ct
    return result

def DecryptCBC(result,u, a):
    v = binpow(u,a)
    sharedkey = str(u+v)
    plainText =  sharedkey.encode('utf-8')
    hashKey = hashlib.sha256(plainText).digest()
    cipher = AES.new(hashKey, AES.MODE_CBC, b64decode(result)[:AES.block_size])
    pt = unpad(cipher.decrypt(b64decode(result)[AES.block_size:]), AES.block_size)
    return pt