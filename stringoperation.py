#string in python

couple = "Rohan & Sonam"
print("Count of characters in couple Variacle ->", len(couple))
print(couple[0])
print(couple[12])

first_char = couple[0]

print("First character of couple variable is ->", first_char)


#clicing start: end
slicing = couple[0:5] # Rohan
print("Slicing of couple variable is ->", slicing)
girl = couple[8:13] # Sonam
print("Slicing of couple variable is ->", girl)

last_char = couple[12]
print("Last character of couple variable is ->", last_char)
last_char1 = couple[-1]
print("Last character of couple variable is ->", last_char1)
last_char2 = couple[-2]
print("Last character of couple variable is ->", last_char2)

#skip characters while slicing
skip_1var = couple[0:13:2]
print("Skip characters while slicing of couple variable is ->", skip_1var)

skip_var = couple[0::2]
print("Skip characters while slicing of couple variable is ->", skip_var)
reverse_string = couple[::-1]
print("Reverse of couple variable is ->", reverse_string)
reverse1_string = couple[::1]
print("Reverse of couple variable is ->", reverse1_string)

#String operations

a= "Rohan"
b ="Sonam"
c= 50
print(a+ " &" + b) #concationation
print(a*3)
print('R' in a)#Membership operators
print('r' in a)#Membership operators
print(len(a)) #length


#Methods in string

message = "   Learn Python!    "

def my_func():
    d = 5
    e = 10
    result = d*e
    print("Result of multiplication is ->", result)
    result2 = result//2
    print(result2)

my_func()
my_func()
my_func()
my_func()


print(message.upper())
print(message.lower())
print(message.strip())
print(message.replace("Python", "Coding"))
print(message.replace("Python", "Coding").strip())
print(message.find("P"))
print(message.count("n"))
print(message.count("P"))
print(message)

message1 = message.replace("Python", "Coding").strip()
print(message1.find("P"))
print(message1.count("n"))
print(message1.count("P"))
print(message1)

message = message.replace("Python", "Coding").strip()
print(message.find("X"))
print(message.count("n"))
print(message.count("P"))
print(message)
print(message.startswith(" "))
print(message.endswith (" "))

csv_data = "apple, banana, mango, orange"
csv_data1 = "apple//banana//mango//orange"

result = csv_data.split(",")
print(result)

result1 = csv_data1.split("//")
print(result1)

#immutable
name3= "syed"

print(name3)
print("current location of name3 variable is ->", id(name3))
print("current location of name3 variable is ->", id(name3))
print("current location of name3 variable is ->", id(name3))
print("current location of name3 variable is ->", id(name3))

name3= "syed ABBAS"
print("current location of name3 variable is ->", id(name3))
name3= name3.lower()
print("current location of name3 variable is ->", id(name3))


#String indexing & Slicing