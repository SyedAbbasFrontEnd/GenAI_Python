print(">>>Welcome to the Python Playground <<<")
name = input("Enter your name here => ")
age = input("Enter your age here => ")
city = input("Tell where are you from => ")

print(f"\n\nHello {name}, it's nice to meet you. {name} is from {city}. He/She was born in {2025-int(age)}.")

num1 = float(input("Ebter the first number here ->"))
num2 = float(input("Ebter the Second number here ->"))

#arthmatic
sumresult = num1+num2
product = num1 * num2
division = num1//num2

#compariosion
is_equal = num1 == num2
is_greater = num1 > num2
is_smaller = num1 < num2

#logical
both_positive = num1 > 0 and num2 > 0
both_negative = num1 < 0 and num2 < 0


print(f"\n\nThe sum of {num1} and {num2} is {sumresult}.")
print(f"The product of {num1} and {num2} is {product}.")
print(f"The division of {num1} and {num2} is {division}.")
print(f"\n\nIs {num1} equal to {num2}? {is_equal}.")
print(f"Is {num1} greater than {num2}? {is_greater}.")
print(f"Is {num1} smaller than {num2}? {is_smaller}.")
print(f"\n\nAre both {num1} and {num2} positive? {both_positive}.")
print(f"Are both {num1} and {num2} negative? {both_negative }.")

print("\nString Manipulation")
print(f"Your Name in upper case -> {name.upper()}")
print(f"Your Name in lower case -> {name.lower()}")
print(f"Your Name in title case -> {name.title()}")
print(f"Your Name in reversed order -> {name[::-1]}")
print(f"Here is the first and last char of your name -> {name[0]}, {name[-1]}")