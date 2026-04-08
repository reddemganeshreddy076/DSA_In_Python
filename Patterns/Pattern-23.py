# Take input
n = int(input(" Enter n : "))

# Logic
for i in range(n):
    print((str(n-i)+' ')*(n-i))

for i in range(n):
    for j  in range(n-i):
        print(str(n-i), end = ' ')
    print()