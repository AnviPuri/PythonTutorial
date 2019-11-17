def add(*args):
    print(args)
    return sum(args)

def traverseDictionary(**kwargs):
    print(kwargs)
    for item in kwargs:
        print(f"{item}:{kwargs[item]}")

traverseDictionary(fruit = 'orange',vegetable = 'brinjal')

print(add(2,3,4))
