class  Animal:
    def eat(self):
        print("this animal eats grass")


class Dog(Animal):
    def bark(self):
        print("dog barks")


d =Dog()
d.eat()
d.bark()