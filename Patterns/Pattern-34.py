# Take input
n = int(input(" Enter n :"))

# Logic 
for i in range(n):
    print('-'*(n-i-1),end= '')
    for j in range(i+1):
        print(str(n-j),end=' ')
    print()