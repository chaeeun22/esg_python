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

'''

a = [3, 7, 1, 9, 8]
a.sort()
a.reverse()
a.insert(1,2)
a.remove(3)
a.pop()
print(a)

