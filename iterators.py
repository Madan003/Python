# 1
movies = ['gaja', 'ayya', 'sarathi', 'bulbul', 'katera']

it = iter(movies)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# 2

class evenNumbers():
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n < 0:
            raise StopIteration
        if self.n % 2 == 0:
            num = self.n
        self.n -= self.n
        return num

e = evenNumbers(10)

for i in e:
    print(e)