# Key-Authenticated-Cryptography

This project develops a "Key Autheticated Cryptography" program in Python 3.7.

Composed by three main programs, and a converter from CSV to XLS.

The files:
 
 - key_generator.py
   Generates the key file.
 
 - password.py
   Asks for website, username/email and password.
   The outputs are a CSV file with website, username/email and password, and a CSV file with website, username/email and encrypted    password.
   
 - decrypted.py
   Asks for the encrypted password and uses the key to decrypt it and return the decrypted password.
   
Package requirements:

1. Cryptography 
2. Python 3.7
3. Pandas
4. Glob
5. Pyexcel

