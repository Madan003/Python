marks = [23,43,54,67,85,43,54,85,43]
counter = {}
for mark in marks:
    if mark not in counter:
        counter[mark] = 1
    else:
        counter[mark] += 1
print(counter)