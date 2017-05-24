#! python3

import sys
import shelve

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name
shelfFile = shelve.open('mydata')
accounts = list(shelfFile.keys())
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats

if account in accounts:
    password = shelfFile[account]
    print('Password for ' + account + ' is ' + password)
else:
    print('There is no account named ' + account)

shelfFile.close()
