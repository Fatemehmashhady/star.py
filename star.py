n = int(input("n: "))
for row in range(1,n+1):
    print("*"*row)
for row in range(1,n+1):
    n = n-1
    print("*"*n)

