# Universidad del Valle de Guatemala
# Lab 10: ElGamal
# Julio Herrera 19402
# Bryann Alfaro 19372
# Diego Arredondo 19422

from gamal import *
from modes import *

option = 0
while (option != '4'):
    menu()
    option = input("\nIngrese la opcion numérica: ")
    if option=='1':
        keys = GenerarClaves()
        private = keys[1]
        print('\nllave privada:')
        print('a: ',private)
        print('\nllave publica con primo generado:')
        print('g: ',keys[0][0])
        print('h: ',keys[0][1])
        print('p: ',keys[0][2])

    elif option == '2':
        message = input('\nIngrese el mensaje a cifrar: ')
        cipher_text = EncryptCBC(message.encode('utf-8'), keys[0])
        print("Mensaje cifrado: ", cipher_text[1])

    elif option == '3':
        mensaje_a_descifrar = input('\nIngrese el mensaje a descifrar: ')
        recovered_message = DecryptCBC(mensaje_a_descifrar,private,cipher_text[0],keys[0][2])
        print("Mensaje recuperado: ", recovered_message)

    elif option == '4':
        print('\nAdios')

    else:
        print('\nOpcion incorrecta')
