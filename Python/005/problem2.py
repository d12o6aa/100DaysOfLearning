# Write a program that takes three numbers as input and prints the largest among them

x = int(input("number 1 : "))
y = int(input("number 2 : "))
z = int(input("number 3 : "))
if x > y:
    if x > z:
        print(x)
    else:
        print(z)
else:
    if y > z:
        print(y)
    else:
        print(z)
