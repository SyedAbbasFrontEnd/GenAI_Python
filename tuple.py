my_tuple =(5)

print(my_tuple)
print(type(my_tuple))

my_tuple =(5,)

print(my_tuple)
print(type(my_tuple))

my_tuple2=("blue", "green", "red", "yellow", "black", "blue")
var1 = my_tuple2.index("blue")
print(f"index of first 'blue' in my_tuple2 is -> {var1}")
print(f"count of 'blue' in my_tuple2 is -> {my_tuple2.count('blue')}")

my_tuple3=(2,4)
my_tuple4=(1,3,5)

var2=my_tuple3 + my_tuple4
print(f"concatenated tuple is -> {var2}")

var3=my_tuple4*3
print(f"repeated tuple is -> {var3}")

info=("syed", 25, "Kolkata", 5.9)
print(info)
#unpacking
name, age, city, height = info
print(f"Name is -> {name}, nice to know that you're from {city} and your age is {age} and your height is {height}")

config = ["server", 5000]
config[1] = "shaktman"
print(config)

# config = ("server", 5000)
# config[1] = "shaktman"
# print(config)