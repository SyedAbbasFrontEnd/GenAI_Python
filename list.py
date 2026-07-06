my_list = ["apple", "banana", "cherry", "date", "elderberry"]
# print(my_list)
# print(type(my_list))
# print(len(my_list))
# print(my_list[1])
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[2:5])


my_lst = ["Rohan", "Saqib", "Abbas"]

print(my_lst)
print(f"Initial location -> {id(my_lst)}")
my_lst[0]= "Rohan"
print(my_lst)
print(f"Current location -> {id(my_lst)}")
my_lst[0]= "Syed"
print(my_lst)
print(f"Current location -> {id(my_lst)}")
my_lst.append("Hussain")
print(my_lst)

my_lst.insert(1, "Developer")
print(my_lst)

Syed_friends = ["jimmy", "Faraz", "Abdullah"]
var1 = "Ajju"
my_lst.extend(Syed_friends)
# my_lst.extend(var1)
print(my_lst)

deleted_name = my_lst.pop()
print(my_lst)
print(deleted_name)

#copying a list
my_lst2 = my_lst.copy()
m