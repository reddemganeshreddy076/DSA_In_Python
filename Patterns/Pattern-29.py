# Take input
n = int(input(" Enter n :"))

# Logic 
for i in range(n):
    print('-'*(n-i-1)+'* '*(i+1))

# No.of Spaces: n-i+1
# no.of Stars: i+1
for i in range(n):
    for j in range(n):
        print(end=' .' )
    print()