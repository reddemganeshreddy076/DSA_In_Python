# Take input
n = int(input(" Enter n :"))

# Logic 
for i in range(n):
    print('-'*(n-i-1),(chr(64+i+1)+' ')*(i+1))


for i in range(n):
    print('-'*(n-i-1),end='' ) #print spaces first
    for j in range(i+1):
        print(chr(65+i),end=' ') #print numbers following to spaces
    print()
# Symbol: 64+i+1
# No.of Spaces:n-i-1
# same symbol repeating so no need of nested loops