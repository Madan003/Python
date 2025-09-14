# searching
string = "karnataka"
a = input("Enter a letter to find: ").lower()
for letter in string:
    if letter.lower() == a:
        print("Letter Found.")
        break
else:
    print("Letter not found.")

#sum of lists values without built in
l = [23,65,756,86,45]
sum = 0
for i in l:
    sum += i
print(sum)

#doubling a list and adding it in another list
x = [29,3,11,21,2005,2007]
y = []

for num in x:
    dl = num*2
    y.append(dl)

print(x)
print(y)

#looping through dictionaries
d = {"name":"madan","age":"20","dream":"Billionaire"}

for key,values in d.items():
    print(f"{key} - {values}")

#adding lists to dictionary
names = ["madan","harshu","ganavi"]
marks = [35,95,85]

students_data = {}

for index,name in enumerate(names):
    students_data[name] = marks[index]

print(students_data)

#another way

for i in range(len(names)):
    students_data[names[i]] = marks[i]

print(students_data)

# list comprention

languages = ["kannada","english","hindi"]

up_lang = [lang.upper() for lang in languages]

print(up_lang)

# dictionary compresntions

subs = ["maths","biology","computer science"]

sub_code = {sub:len(sub) for sub in subs}

print(sub_code)

# list input

m = input("Enter list items: ")

n = [int(item) for item in m.split()]

print(n)
