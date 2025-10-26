#task1
t = ("madan",29,2005,20,"gowda")

print(t[1:3])

t2 = ("harshhu",31,2007,18,"gowdthi")

t3 = t + t2
print(t3)

#task 2
fruits_1 = {"muskmelon","chikku","mango","butterfuit"}
fruits_2 = {"muskmelon","watermelon","mango","abc"}

print(fruits_1 | fruits_2)
print(fruits_1 & fruits_2)
print(fruits_1 - fruits_2)

fruits_1.add("banana")
print(fruits_1)

fruits_1.discard("chikku")
print(fruits_1)

#task 3
l = [10,20,30,40,50]

print(l)
print(type(l))
print(l[::-1])

t = tuple(l)

print(t)
print(type(t))

s = set(l)

print(s)
print(type(s))

s.add(60)

print(s)