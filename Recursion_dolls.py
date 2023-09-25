def openDolls(dolls):
    if dolls==1:
        print('this is last doll')
    else:
        openDolls(dolls-1)
        print(f'this is {dolls-1} doll')

openDolls(3)        

