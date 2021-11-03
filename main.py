from gamal import *
from modes import *
import pyDH
import hashlib
import base64

#Segunda parte

keys = GenerarClaves()

private = keys[1]


option = ''
while (option != 'salir'):
    option = input("\nIngrese la opcion: 'enviar', 'recibir' o 'salir': ")
    if option == 'enviar':
        message = input('\nIngrese el mensaje a cifrar: ')
        print("Mensaje original: ", message)
        cipher_text = EncryptCBC(message.encode('utf-8'), keys[0])
        print("Mensaje cifrado: ", cipher_text[1])

    if option == 'recibir':
        mensaje_a_descifrar = input('\nIngrese el mensaje a descifrar: ')

        recovered_message = DecryptCBC(mensaje_a_descifrar,private,cipher_text[0],keys[0][2])
        print("Mensaje recuperado: ", recovered_message)

    if option == 'salir':
        print('\nAdios')
