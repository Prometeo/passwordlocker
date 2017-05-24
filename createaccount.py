#! python3

import sys
import shelve

if len(sys.argv) is not 3:
    print('Usage: python pw.py [account] [password]')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name
password = sys.argv[2]     # second command line arg is the account password
shelfFile = shelve.open('mydata')
shelfFile[account] = password
shelfFile.close()
