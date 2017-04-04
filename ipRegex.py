#Author: Lukasz Sztukowski
#ipRegex.py  # searches for IP in clipboard and paste them to clipboard

import pyperclip, re

ipRegex = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]"
                     , re.VERBOSE)

text = str(pyperclip.paste())
matches = []


for list in ipRegex.findall(text):
    ipResults = ''.join([list])
    matches.append(ipResults)

    
# Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No IP addresses found.')
