import numpy as np
import random
import base64
import hashlib

def gcd(a,b):
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def egcd(a, b):
    xp  = 0
    yp = 1
    if a == 0:
        return b, xp, yp
    else:
        gcd, x, y = egcd(b % a, a)
        xp = y - (b // a) * x
        yp = x
        return gcd,xp, yp


def modInverse(a,n):

    g,x,y =egcd(a,n)
    if(g!=1):
        return 'No existe inverso'
    else:
        res = x%n
        return res
def binpow(a,b):
    if b==0:
        return 1
    result = binpow(a,b//2)
    if b % 2:
        return result * result *a
    else:
        return result*result

def testFermat(n,k):
    prime = True
    pruebas = []
    for i in range(0,k):
        a = np.random.randint(2,n-2)
        pruebas.append(a)
        if (binpow(a,n-1)%n)!=1:
            prime = False
    if prime:
        return prime,pruebas
    else:
        return prime,a

def generatorPrimes(longitud,cantidad):
    numb = '1'+(longitud-1)*'0'
    numb = int(numb)
    primos = []
    while len(primos) < cantidad:
        numero = np.random.randint(numb, numb*10-1000)

        if testFermat(numero,5)[0]==True:

            primos.append(numero)
        else:
            pass
    return primos
def GenerarClaves():
    p = generatorPrimes(4,2)
    p = p[0]

    g = np.random.randint(2,p-1)

    a = np.random.randint(2,p-1)


    while gcd(g,p-1)!=1:
        g = np.random.randint(2,p-1)

    h = pow(g,a,p-1)
    b = np.random.randint(2,p-1)
    u = pow(g,b)
    v = pow(h,b)
    sharedkey = str(u+v)
    plainText =  sharedkey.encode('utf-8')
    hashKey = hashlib.sha256(plainText).digest()
    private = a
    public = g,h
    public = str(public).encode('ascii')
    publickey = base64.b64encode(public).decode()
    private = str(private).encode('ascii')
    privatekey = base64.b64encode(private).decode()
    return publickey,privatekey,hashKey,u,a


def menu():
    print("Ingrese la opcion:")
    print('1. Generar claves')
    print('2. Encriptar mensaje')
    print('3. Decriptar mensaje')
    print('4. Salir')

