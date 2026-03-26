# class Animal:
#     def speak(self):
#         print("Animals speaks")

# class Dog(Animal):
#     def bark(self):
#         print("Dogs barks")

# d = Dog()
# d.speak()
# d.bark()


class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

# for animal in (Cat(), Dog()):
#     animal.sound()
cat = Cat()
Cat.sound(cat)
dog = Dog()
Dog.sound(dog)  

