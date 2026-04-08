# Take input
n = int(input(" Enter n :"))

# Logic 
for i in range(n):
    for j in range(n-i):
        print(chr(64+n-j), end=' ')
    print()