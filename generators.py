class Animal:
    def sound(self):
        print('animal sound')

class Dog(Animal):
    def sound(self):
        super().sound()
        print('bark')

class Cat(Animal):
    def sound(self):
        print('meow')


d = Dog()
d.sound()