import pretty
import random

# Task 34. Создать класс Годзила. У данного класса должен быть атрибут - объем желудка.
# Написать для данного класса метод поедания людей. В данную функцию должен
# передаваться объем съеденного и соответственно уменьшаться место в желудке.
# Когда Годзила заполнит желудок на 90%, метод должен выводить надпись, что
# Годзила наелся и больше не может поедать людей.

pretty.pretty_task(34)

class Godzilla:


    PERSENT = 0.1

    def __init__(self,eaten_human_volume=0,volume_of_stomach = 1000):
        self.eaten_human_volume = eaten_human_volume
        self.volume_of_stomach = volume_of_stomach
        self.last_volume = volume_of_stomach

    def eat_humans(self,eat_human):
        if self.last_volume - eat_human == Godzilla.PERSENT*self.volume_of_stomach:
            print("Godzilla is full and can no longer eat people")

        else:
            self.last_volume -= eat_human




dinner = Godzilla()

while dinner.last_volume > Godzilla.PERSENT*dinner.volume_of_stomach:
    dinner.eaten_human_volume = random.randint(1,120)
    if dinner.last_volume - dinner.eaten_human_volume < Godzilla.PERSENT*dinner.volume_of_stomach:
        continue
    elif dinner.last_volume - dinner.eaten_human_volume == Godzilla.PERSENT*dinner.volume_of_stomach:
        print("Last human:", dinner.eaten_human_volume, "nym nym nym nym nym")
        dinner.eat_humans(dinner.eaten_human_volume)
        break
    else:
        dinner.eat_humans(dinner.eaten_human_volume)
        print("Human:",dinner.eaten_human_volume,"nym nym nym","Last volume:", dinner.last_volume)


