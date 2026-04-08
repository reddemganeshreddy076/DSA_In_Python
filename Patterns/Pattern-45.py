#Take Input
n = int(input(" Enter n: "))

# Logic
for i in range(n):
    print('-'*(n-i-1),(chr(65+i)+' ')*(i+1))

for i in range(n-1):
    print('-'*(i+1),(chr(63+n-i)+' ')*(n-i-1))