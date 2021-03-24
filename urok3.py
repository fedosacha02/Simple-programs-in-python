name = input("Введите имя персонажа: \n")
familia = input("Введите фамилию персонажа: \n")
move = input("Введите движение персонажа: \n")
jump = input("Введите силу пріжка персонажа: \n")
try:
    jump = int(jump)
except ValueError:
    print("Вы ввели неправильное значение !")
class Person():
    def __init__(self, name, familia, moving_person, jumping):
        self.name = name
        self.familia = familia
        self.moving_person = moving_person
        self.jumping = jumping
    def move(self):
        print(f"Персонаж по имени {self.name} и с фамилией {self.familia} переместился на {self.moving_person}")

    def jump(self):
        print(f"Персонаж по имени {self.name} и с фамилией {self.familia} прігнул на вісоту {self.jumping}")
first = Person(name,familia,move,jump)
print(first.jump())
print(first.move())