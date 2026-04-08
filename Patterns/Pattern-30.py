# Take input
n = int(input(" Enter n :"))

# Logic 
for i in range(n):
    print('-'*(n-i-1),(str(i+1)+' ')*(i+1)) # use repetition operator

for i in range(n):#use nested loops
    print('-'*(n-i-1),end = '') #print spaces first
    for j in range(i+1):
        print(str(i+1), end = ' ') #print numbers following to spaces
    print() 

# NO.of Spaces: n-i-1
# Numbers : str(i+1) of (i+1) times 
# same number  repeating so no need of nested loops