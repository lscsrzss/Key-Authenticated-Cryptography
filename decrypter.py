# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:42:19 2019

@author: Luis Rodriguez
"""

from cryptography.fernet import Fernet

file = open('key.key','rb')
key=file.read()
file.close()

encrypted=input('Enter the encrypted password: ')
encrypted=encrypted.encode()

f=Fernet(key)
decrypted=f.decrypt(encrypted)
decrypted=decrypted.decode()
print('\n')
print('Your password is: ',decrypted)

print('\n')
exit=input('Press enter to quit.' )