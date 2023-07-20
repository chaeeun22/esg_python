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


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print(set1 & set2)
print(set1 | set2)


a = "student"
if a == "student":
    print("hello")
else:
    print("nope")


score = int(input("점수가 몇점인가요? "))

if score >= 90 and score <= 100:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


a = ["A", "B", "C", "D"]

for i in range(len(a)):
    print(a[i])


def say_hello(name):
    print("hello", name)

say_hello("채은")

print(abs(-3.5))

a = 3
print(id(a))


def positive(x):
    return x > 0
b = [1, 4, -7, 2, 9, -5]
print(list(filter(positive, b)))



colors = ["white", "red", "brown", "blue"]
names = ["Lukas", "Mike", "Yoon", "Lee"]

for i, name in enumerate(names):
    print(name, f"likes color {colors[i]}")

a = [2, 55, 24, 78, 157]
print(max(a))
print(min(a))

print(type("abc"))

import os
print(os.getcwd())
print(os.name)

'''

import time

print(time.time())
