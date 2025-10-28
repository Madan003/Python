def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result

print(subsets([1, 2, 3]))

#xor sum of all subsets
d = [1,3]
res = 0
for i in d:
    res|=i
print(res<<len(d)-1)
print(bin(9)[2:])
print(bin(9)[2:5])