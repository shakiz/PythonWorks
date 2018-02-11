friends={'Shakil':'16 may','Jahid':'4th February','Imran':'1st January'}
value=True
while value==True:
    print('Enter name or key:')
    name=input()
    if name=='':
        break;
    if name in friends:
        print('',name,' birthday is on ',friends[name])
    else:
        print('No matching value found')
        print('Do you want to insert it into datatbase??')
        print('Type yes for insert or no for deny..')
        check=input()
        print('Enter birth date:')
        bday=input()
        if check=='yes' or check=='Yes':
            friends[name]=bday
        else:
            break
            value=False
            
