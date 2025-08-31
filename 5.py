items = ["Redlabel","milk","sugar"]

#slicing
print(items[::2])

l = [1,2,3,4,5,False]

#list functions
print(sum(l))

a = [20,40,60,80,100,120,140]

print(a)

#Adding a new item to the end of the list
a.append(160)

print(a)

#Adding at the second position
a.insert(1,30)

print(a)

#Remove the third item from the list
a.pop(2)

print(a)

b = [27,21,29,31,3,30,6]

print(b)

#sorting in ascending order
b.sort()

print(b)

#sorting in descending order
b.sort(reverse=b)

print(b)

#reversing a list
b.reverse()

print(b)