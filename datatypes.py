#IN this code I'm assigning different values to different data types and checking their output and
# types

print("Hello World")

x = int(3)
print(type(x))
print(x)
y = float(0.5)
print(type(y))
print(y)
z = complex(50j)
print(type(z))
print(z)
a = list(("a", "e", "i", "o", "u"))
print(type(a))
print(a)
b = tuple(("Pavan", "Chetan", "Puthin"))
print(type(b))
print(b)
c = range(6)
print(type(c))
print(c)
d = dict(name="Chetan", age=24)
print(type(d))
print(d)
e = set(("pav", "che", "put"))
f= tuple(("Pavan", "Chetan", "Puthin"))
g = bool(5)
h = bytes(5)
i = bytearray(5)
j = memoryview(bytes(5))
print(e,f,g,h,i,j);
print(type(e,f,g,h,i,j));
