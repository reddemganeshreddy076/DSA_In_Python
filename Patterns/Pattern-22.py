# Take input
n = int (input(" Enter n : "))

# Logic 
for i in range(n):
    print((chr(65+i)+'  ')*(n-i) ) 

for i in range(n):
    for j in range(n-i):
        print(chr(65+i), end = ' ')
    print()