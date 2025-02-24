#take input from the user limited to inclusive range 1-8
n = 0
while n<=0 or n>8:
    n = int(input('Enter a number between 1-8: '))

#simple increasing block
for i in range(1, n+1):
    print("#" * i)

#inverted increasing block
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("#" * i, end="")
    print(" ")

#simple decreasing block
for i in range(n, 0, -1):
    print("#" * i)

#inverted decreasing block
for i in range(n, 0, -1):
    print(" " * (n-i), end="")
    print("#" * i, end="")
    print(" ")

#combined increasing block
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("#" * i, end="")
    print("  ", end="")
    print("#" * i)

#combined decreasing block
for i in range(n, 0, -1):
    print(" " * (n-i), end="")
    print("#" * i, end="")
    print("  ", end="")
    print("#" * i)

#combined decreasing block
for i in range(n, 0, -1):
    print(" " * (n-i), end="")
    print("#" * i, end="")
    print("  ", end="")
    print("#" * i)

#combined increasing block
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("#" * i, end="")
    print("  ", end="")
    print("#" * i)