#take input from the user
n = 0
m = 0
while n<=0 or m<=0:
    n = int(input('Enter a number of columns between 1-8: '))
    m = int(input('Enter a number of hashes between 1-8: '))

#simple increasing block
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("#" * m)

