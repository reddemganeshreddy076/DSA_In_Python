# Take input
n= int(input(' enter n:'))

# Logic
for i in range(n):
    print((chr(65+i)+' ')*(i+1))
for i in range(n-1):
    print((chr(64+n-i-1)+' ')*(n-i-1))