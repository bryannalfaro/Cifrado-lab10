import numpy as np

def gcd(a,b):
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

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
    a = np.random.randint(2,p-1) # privada

    while gcd(g,p-1)!=1:
        g = np.random.randint(2,p-1)

    h = pow(g,a) # g^a
    return (g,h,p),a


def menu():
    print("\nIngrese la opcion:")
    print('1. Generar claves')
    print('2. Encriptar mensaje')
    print('3. Decriptar mensaje')
    print('4. Salir')
