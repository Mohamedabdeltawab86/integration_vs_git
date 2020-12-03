n = 0
while n<=0 or n>8:
    n = int(input('Enter a number between 1-8: '))

for i in range(1, n+1):
    print("#" * i)


for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("#" * i, end="")
    print(" ")

