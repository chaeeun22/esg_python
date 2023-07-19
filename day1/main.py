'''
random_list = [3, 3.9, "python", True]

print (random_list)

print(random_list[1])

a = "Hello"
print(a[0])
print(len(a))
print(a[:5])
print(a[1:5])
print(random_list[2])

print(".".join(a))

b = "    hi     "
print(b.lower())
print(b.upper())
print(b.strip())

c = "Life is too short"
print(c.replace("short", "long"))
print(c.split())
print(c.split("s"))


a = [1, 2, 3]
del(a[1])
a.append(4)
a.extend(["a", "b", "c"])
print(a)



a = [3, 7, 1, 9, 8]
a.sort()
a.reverse()
a.insert(1,2)
a.remove(3)
a.pop()
print(a)


my_dictionary = {"name": "김채은"}
print(my_dictionary)
my_dictionary["age"] = 22
print(my_dictionary)
my_dictionary["favorite food"] = [{"name": "pizza", "is_healthy": False}]
print(my_dictionary)
print(my_dictionary["name"])
print(my_dictionary.get("adress", "Unknown"))

for key, value in my_dictionary.items():
    print("key:", key)
    print("value:", value)
'''

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print(set1 & set2)
print(set1 | set2)
