from datetime import date


class Person:
    def __init__(self, first, last, birth):
        self.first_name = first
        self.last_name = last
        self.birth_date = birth

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year

        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age = age - 1

        return age


class Female(Person):
    def age(self):
        age = super().age()

        if age > 20:
            age = 20

        return age
