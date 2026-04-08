# Take Input

n = int(input("Enter n: "))

# Logic
for i in range(n):
    print(' - '*(n-i-1),str(i+1),end = '')
    if(i>0):
        print(' - '* (2*i-1),str(i+1),end = '')
    print()