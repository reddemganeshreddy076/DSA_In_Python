# Take input
n = int(input(" Enter n :"))

# Logic 
for i in range(n):
    print('-'*i,'* '*(n-i))
for i in range(n):
    print('-'*(i),end = '')
    for j in range(n-i):
        print('*', end = ' ')
    print()