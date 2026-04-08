#Take Input

n = int(input("Enter n :  "))
#Logic 
for i in  range(n):
    for j in range(n-i):
        print(j+1, end =  '  ')
    print()

for i in  range(n):
    for j in range(n-i):
        print(str(j+1)+' ',end='')
    print()