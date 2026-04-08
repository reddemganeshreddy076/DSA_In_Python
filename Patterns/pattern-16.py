# Take Input
n = int(input('Enter n: '))
# Logic

for i in range(n):
    for j in range(i+1):
        print(str(j+1),end=' ')
    print()