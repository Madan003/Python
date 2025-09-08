#task 1
famous_dishes = {
    "bengalore": "Biriyani",
    "mysore": "mysore pak",
    "shivamogga": "kadubu",
    "davanagere": "benne dosa",
    "mangaluru": "fish"
}

print(famous_dishes)

famous_dishes["raichur"] = "joladha rotti"

print(famous_dishes)

famous_dishes["bengalore"] = "pizza"

print(famous_dishes)

x = famous_dishes.pop("mangaluru")

print(x)
print(famous_dishes)

print(famous_dishes.keys())

print(famous_dishes.values())

#task 2
friends = {
    "friend 1":{
        "name": "kiran",
        "fvrt_sub": "maths",
        "fvrt_food": "rotti"
    },
    "friend 2":{
        "name": "jeevan",
        "fvrt_sub": "kannada",
        "fvrt_food": "dosa"
    }
}

print(friends)
print(type(friends))

print(friends["friend 2"]["fvrt_food"])

