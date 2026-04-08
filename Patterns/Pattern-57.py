# Take input
n= int(input(' enter n:'))

# Logic
for i in range(n):
    print(' - '*((n-i-1)),end='')
    for j in range(i+1):
        print('* ',end='')
    print()

for i in range(n-1):
    print(' - '*(i+1),end='')
    for j in range(n-i-1):
        print(' * ' ,end = '')
    print()

    print('\n \n')
    
    for i in range(n):
        print(' - '*(n-i-1),' * '*(i+1))
    
    for i in range(n-1):
        print(' - '*(i+1),' * '*(n-i-1))


