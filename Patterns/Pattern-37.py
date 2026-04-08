# Take input
n = int(input(" Enter n :"))

# Logic 
for i in range(n):
    print('-'*(i),(str(i+1)+' ')*(n-i))

for i in range(n):
    print('-'*(i), end='')
    for j in range(n-i):
        print(i+1,end=' ')
    print()