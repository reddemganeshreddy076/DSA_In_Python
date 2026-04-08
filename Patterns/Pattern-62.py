# Take Input

n = int(input("Enter n: "))

# Logic
for i in range(n):
    print('- '*(n-i-1),end = ' ')
    for j in range(i+1):
        print(n-j,end = ' ')
    print()

for i in range(n-1):
    print('- '*(i+1),end = ' ')
    for j in range(n-i-1):
        print(n-j,end = ' ')
    print()