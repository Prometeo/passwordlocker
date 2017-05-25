#! python3

import sys
import shelve
from AESCipher import AESCipher

# if len(sys.argv) is not 3:
#     print('Usage: python pw.py [account] [password]')
#     sys.exit()

account = sys.argv[1]      # first command line arg is the account name
password = sys.argv[2]     # second command line arg is the account password
shelfFile = shelve.open('mydata')
cipher = AESCipher('secretpassword')
shelfFile[account] = str(cipher.encrypt(password))
shelfFile.close()
