n = int(input())
m = input()
t=[int(item) for item in m.split()]
t = tuple(t)
print(t)
print(hash(t))