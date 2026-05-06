# 7
class Laptop:
    def __init__(self, brand, ram, storage, serial):
        self.brand = brand
        self._ram = ram
        self._storage = storage
        self.__serial = serial

    def upgrade_ram(self, x):
        self._ram += x

    def upgrade_storege(self, x):
        self._storage += x

    def info(self):
        print(f"brand: {self.brand}, ram: {self._ram}, storage: {self._storage}, serial: {self.__serial}")


l1 = Laptop("S26 ULTRA", 8, 256, "kjeqfl")
l1.upgrade_ram(8)
l1.upgrade_storege(256)

l1.info()

# 8
class Teacher:
    def __init__(self, name, subject, salary):
        self.name = name
        self._subject = subject
        self.__salary = salary

    def teach(self, hours):
        self._subject += hours

    def increase_salary(self, x):
        self.__salary += x

    def info(self):
        print(f"name: {self.name}, subject: {self._subject}, salary: {self.__salary}")


t1 = Teacher("Jamshid", 0, 800)

t1.teach(2)
t1.increase_salary(400)
t1.info()

# 9
class GameCharacter:
    def __init__(self, name, health, level, power):
        self.name = name
        self._health = health
        self._level = level
        self.__power = power

    def attack(self):
        print(self._health - 10)

    def heal(self, x):
        self._health += x

    def level_up(self):
        self._level += 2


g1 = GameCharacter("Jemfur", 90, 0, 10)
g1.attack()
g1.heal(10)
g1.level_up()

# 10
class Movie:
    def __init__(self, title, duration, rating):
        self.title = title
        self._duration = duration
        self.__rating = rating

    def play(self):
        print("Clash")

    def rate(self, x):
        self.__rating += x

    def info(self):
        print(f"title: {self.title}, duration: {self._duration}, rating: {self.__rating}")


m1 = Movie("Playing Avengers", 10, 8)
m1.play()
m1.rate(1)
m1.info()

# 11
class Animal:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def eat(self):
        print("Eating...")

    def sleep(self):
        print("Sleeping...")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._breed = breed

    def bark(self):
        print("Woof")

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Breed: {self._breed}")
        self.eat()
        self.bark()


dog = Dog("Rex", 5, "Ovchi")
dog.info()

# 12
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
            super().__init__(name, age)
            self._grade = grade

    def study(self):
        print("Studying...")

    def take_exam(self):
        print(f"Grade: {self._grade}")


s1 = Student("Jamshid", 16, 85)
s1.study()
s1.take_exam()
