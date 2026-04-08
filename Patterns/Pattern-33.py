# Take input
n = int(input(" Enter n :"))

# Logic 
for i in range(n):
    print('-'*(n-i-1),end = '')#print spaces for each row
    for j in range(i+1):
        print(chr(65+j),end=' ')#print symbols following to spaces
    print()
