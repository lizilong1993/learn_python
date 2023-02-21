class Dog:
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def bark(self):
        print("Woof!")


my_dog = Dog("Rex", "meat")
print(f"{my_dog.name} is eating {my_dog.food}.")
input("Your dog is ready to bark. Press Enter to continue...")
my_dog.bark()
