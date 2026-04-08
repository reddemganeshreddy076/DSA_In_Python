#Take Input
n = int(input(" Enter n: "))

# Logic 
for i in range(n):
    for j in range(n-i):
        print(i+1, end = ' ')
    print()

for i in range(n):
    print((str(i+1)+ ' ')*(n-i))