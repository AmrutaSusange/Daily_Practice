class Handsome:
    def __init__(self, personality, fitness):
        self.personality = personality
        self.fitness = fitness

class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"hi my name is {self.name} and my age is {self.age}")

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight

    def talk(self):
        print("Bark!")

class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def talk(self):
        print("Meow!")


if __name__ == "__main__":
    mew = Cat("Mew", 2, 'orange')
    mew.speak()
    print(mew.color)
    mew.talk()
