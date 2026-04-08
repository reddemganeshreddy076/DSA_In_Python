# Take input
n= int(input(' enter n:'))

# Logic
for i in range(n):
    print(' - '*(n-i-1),(chr(65+i)+'  ')*(i+1))

for i in range(n-1):
    print(' - '*(i+1),(chr(64+n-i-1)+'  ')*(n-i-1))