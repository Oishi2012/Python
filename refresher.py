print('Star pattern')
for row in range (1,6):
    for stars in range(row):
        print('*',end='')
    print('\n')

print('Reverse star pattern')
for row in range (6,1,-1):
    for stars in range(row):
        print('*',end='')
    print('\n')