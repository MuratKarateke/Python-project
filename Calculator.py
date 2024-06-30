print("Please enter first number.\n")
x = float(input())
print("Please enter second number.\n")
y = float(input())
print("Choose your operator to make an equation.\n")
z = input()

if z == "+":
    result = x + y
elif z == "-":
    result = x - y
elif z == "/":
    result = x / y
elif z == "*":
    result = x * y
else:
    result = "Invalid operator"

print("The result:\n", result)