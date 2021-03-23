name = input("Введите имя персонажа: \n")
familia = input("Введите фамилию персонажа: \n")
move = input("Введите движение персонажа: \n")
jump = int(input("Введите силу пріжка персонажа: \n"))
class Person(name, familia, move, jump):
    def __init__(self, name, familia, moving_person, jumping):
        self.name = name
        self.familia = familia
        self.moving_person = moving_person
        self.jumping = jumping
    def move(self):
        print(f"Персонаж по имени {self.name} и с фамилией {self.familia} переместился на {self.moving_person}")

    def jump(self):
        print(f"Персонаж по имени {self.name} и с фамилией {self.familia} прігнул на вісоту {self.jumping}")
try:
    first_person = Person(name, familia, move, jump)
    first_person.move()
    first_person.jump()
except:
    print("Ві ввели неправильное число!Попробуйте снова!")
    Person(name, familia, move, jump)
