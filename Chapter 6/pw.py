#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'sampleemailpassword1',
             'linkedin': 'samplelinkedinpassword2',
             'Twitter': 'sampletwitterpassword3'}

# pyperclip allows password to be copied to the clipboard
import sys, pyperclip
# command line arguments are stored in sys.argv
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
