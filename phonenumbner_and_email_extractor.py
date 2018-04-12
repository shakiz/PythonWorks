#importing modules
import pyperclip,re

#phone number regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{4})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{6})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

#email regex
emailregex=re.compile(r'''(
    [a-zA-Z0-9]+ #username
    @ #@ symbol
    [a-zA-Z]+ # domain name
    .
    [a-zA-Z]
)''',re.VERBOSE)

#entering the copied text by pyperclip module
text=str(pyperclip.paste())

#taking a list
matches=[]

#grabing all the possible matching values of phone number
for groups in phoneRegex.findall(text):
    phonenum='-'.join([groups[1],groups[3],groups[5]])
    if groups[8]!='':
        phonenum+=' x'+group[8]
    matches.append(phonenum)

#grabing all the possible matching values of email ids
for groups in emailregex.findall(text):
    matches.append(groups)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails are found.')
    
