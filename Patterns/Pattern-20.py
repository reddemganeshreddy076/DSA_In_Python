# Take Input
n = int(input('Enter n: '))
# Logic

for i in range(n):
    print('* '*(n-i))

print('\n \n')

for i in range(n,0,-1):
    print('* '*i)