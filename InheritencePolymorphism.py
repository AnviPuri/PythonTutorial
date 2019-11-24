#Abstract class
class Animal():

    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):

    def who_am_i(self):
        print("I am a pup")

    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):

    def who_am_i(self):
        print("I am a Kitten")

    def speak(self):
        return self.name + " says meow!"

dog = Dog("Felix")
dog.who_am_i()
print(dog.speak())

cat = Cat("Genny")
cat.who_am_i()
print(cat.speak())