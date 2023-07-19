'''
a = "Dog is love"
print(a)
print(a[7:])
print(a.replace("Dog", "Cat"))

b = "lalalalalalalalalala"
print(len(b))
print(b.count("a"))

c = "010-1234-5678"
print(c.replace("-", ""))

x = "hello"
y = "python"
print(x + "! " + y)


color = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white"]
color.remove("green")
print(color)
color.insert(1, "pink")
print(color)


a = {"A": 90, "B": 80, "C": 70, "D": 60}
print(a["B"])

'''

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

print(set1 & set2)
print(set1 - set2)

a = list(set([1, 2, 3, 4, 4, 4, 9, 11, 11, 14]))
print(a)

