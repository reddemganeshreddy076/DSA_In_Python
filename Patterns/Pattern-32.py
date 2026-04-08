# Take input
n = int(input(" Enter n :"))

# Logic 
for i in range(n):
    print(('-')*(n-i-1),end = ' ')#print spaces first
    for j in range(i+1):
        print(str(j+1)+' ',end='') #print numbers following to spaces
    print()
    # Note: Repetition operator wont work here . because, numbers are changing in each row