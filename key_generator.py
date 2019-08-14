# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:35:03 2019

@author: Luis Rodriguez
"""

from cryptography.fernet import Fernet

# Generar llave
key=Fernet.generate_key()
print(key)

file = open('key.key','wb')
file.write(key)
file.close()

print('\n')
exit=input('Key succesfully generate. \nPress enter to quit.' )
