# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:16:33 2019

@author: Luis Rodriguez
"""

archivo= open('Passwords.csv','a')
archivo_encrypted=open('Encrypted Passwords.csv','a')
sitio= input('Website name: \n')
usuario= input('User/Email: \n')
contraseña= input('Password: \n')


# Encriptado de constraseña
from cryptography.fernet import Fernet

# Encrypt

file = open('key.key','rb')
key=file.read()
file.close()

encoded_contraseña=contraseña.encode()
f=Fernet (key)
encrypted=f.encrypt(encoded_contraseña)
#print(encrypted)
encrypted = encrypted.decode()

# Crear Archivo Normal

archivo.write(sitio)
archivo.write(',')
archivo.write(usuario)
archivo.write(',')
archivo.write(contraseña)
archivo.write('\n')

archivo.close()

# Crear archivo con passwords encriptados

archivo_encrypted.write(sitio)
archivo_encrypted.write(',')
archivo_encrypted.write(usuario)
archivo_encrypted.write(',')
archivo_encrypted.write(encrypted)
archivo_encrypted.write('\n')

archivo_encrypted.close()

print('\n')
exit=input('Data stored succesfully. \nPress enter to quit.' )