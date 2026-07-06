# arithmatic

a= 10
b= 3

print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Floor Division:", a//b)
print("Modulus:", a%b)
print("Exponent:", a**b)

#comparision operators
# == != > < >= <=

print("Is a equal to b:", a==b)
print("Is a not equal to b:", a!=b)
print("Is a greater than b:", a>b)
print("Is a less than b:", a<b)
print("Is a greater than or equal to b:", a>=b)
print("Is a less than or equal to b:", a<=b)

#logical operators
# and or not
x=True
y=False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

age = 20
has_license = True

#and operator
print("Eligible to drive:", age >= 18 and has_license)
#or operator
is_citizen = False
has_visa = True
print("Eligible to travel abroad:", is_citizen or has_visa)

#not
is_admin = False
a=10
print("Access granted:", not is_admin)
print(not(a>5))