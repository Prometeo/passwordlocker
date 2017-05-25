#! python3

import sys
import shelve
from AESCipher import AESCipher

if len(sys.argv) is not 2:
    print('Usage: python pw.py [account]')
    sys.exit()

cipher = AESCipher('secretpassword')
account = sys.argv[1]
shelfFile = shelve.open('mydata')
accounts = list(shelfFile.keys())

if account in accounts:
    password = cipher.decrypt(shelfFile[account])
    print('Password for ' + account + ' is ' + password)
    pass
else:
    print('There is no account named ' + account)

shelfFile.close()
