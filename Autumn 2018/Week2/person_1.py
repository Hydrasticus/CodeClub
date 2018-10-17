class Person:
    def __init__(self, first, last, birth):
        self.first_name = first
        self.last_name = last
        self.birth_date = birth

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
