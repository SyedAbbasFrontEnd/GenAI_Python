#fString & docString

# Hello everyone, meet Syed. Syed is from Varanasi. syed is a professional Data Scientist


name = "Syed"
city = "Varanasi"

print("Hello everyone, meet",name, ". ",name, "is from ",city,". ",name," is a professional Data Scientist.")
print(f"Hello everyone, meet {name}. {name} is from {city}. {name} is a professional Data Scientist.")

a = 10
b =2

print(f"{a} x {b} = {a*b}")

a = 10
b =3

print(f"{a} / {b} = {a/b}")
print(f"{a} / {b} = {a/b:.2f}")

#docStrings

def my_simple_func():
    """
    This is a simple function that demonstrates the use of docstrings.
    """
    x = 10
    y = 3
    product = x * y
    result = product // 2
    print(result)

# my_simple_func()
# my_simple_func()
# my_simple_func()
# my_simple_func()
# my_simple_func()
# my_simple_func()

my_simple_func()
print(my_simple_func.__doc__)
