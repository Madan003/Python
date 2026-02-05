# 1
# n = 5
# for i in range(n):
#     print("*"*n)

# 2
# n = 5
# for i in range(1,n+1):
#     print("*"*i)

# 3
# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# 4
# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

# 5
# n = 5
# while n >= 1:
#     print("*"*n)
#     n -= 1

# 6
# n = 5
# for i in range(n, 0, -1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# 7
# n = 5
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*i,end="")
#     if i > 1:
#         print("*"*(i-1))
#     else:
#         print()

# 8
# n = 5
# for i in range(n,0,-1):
#     print(" "*(n-i),end="")
#     print("*"*i,end="")
#     if i > 1:
#         print("*"*(i-1))
#     else:
#         print()

# 9
# it is just printing upside traingle as 7, and down side triangle as 8

# 10
# n = 5
# for i in range(1,n+1):
#     print("*"*i)
# for i in range(n-1,0,-1):
#     print("*"*i)

# 11
# n = 5
# for i in range(1,n+1):
#     if i % 2 == 0:
#         print("01"*(i//2))
#     else:
#         print("1",end="")
#         print("01"*((i-1)//2))

# 12
# n = 5
# s = n*2 - 2
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print(" "*s,end="")
#     s -= 2
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()

# 13
# n = 5
# j = 1
# for i in range(1,n+1):
#     for x in range(1,i+1):
#         print(j,end=" ")
#         j += 1
#     print()

# 14
# n = 5
# for i in range(1,n+1):
#     x = 65
#     for j in range(1,i+1):
#         print(chr(x),end=" ")
#         x += 1
#     print()

# 15
# n = 5
# for i in range(n,0,-1):
#     x = 65
#     for j in range(1,i+1):
#         print(chr(x),end=" ")
#         x += 1
#     print()

# 16
# n = 5
# x = 65
# for i in range(1,n+1):
#     print(chr(x)*i)
#     x += 1

# 17
# n = 5
# for i in range(1,n+1):
#     x = 65
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(chr(x),end="")
#         x += 1
#     if i>1:
#         x = 65 + (i-2)
#         for j in range(i-1):
#             print(chr(x),end="")
#             x -= 1
#     print()

# 18
# n = 5
# for i in range(1,n+1):
#     x = 65 + n 
#     for j in range(i, 0, -1):
#         print(chr(x - j),end=" ")
#     print()

# 19
# n = 5
# space = n * 2 - (n*2-2)
# for i in range(n, 0, -1):
#     print("*"*i,end="")
#     if i<n:
#         print(" "*space,end="")
#         space += 2
#     print("*"*i)

# space = n * 2 - 2
# for i in range(1,n+1):
#     print("*"*i,end="")
#     print(" "*space,end="")
#     space -= 2
#     print("*"*i)

# 20
# n = 5
# space = n * 2 - 2
# for i in range(1,n+1):
#     print("*"*i,end="")
#     print(" "*space,end="")
#     print("*"*i)
#     space -= 2

# space = n * 2 - (n*2-2)
# for i in range(n - 1, 0, -1):
#     print("*"*i,end="")
#     print(" "*space,end="")
#     space += 2
#     print("*"*i)

# 21
# n = 10
# for i in range(1,n+1):
#     if i == 1:
#         print("*"*n)
#     elif i == n:
#         print("*"*n)
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*")

# 22
