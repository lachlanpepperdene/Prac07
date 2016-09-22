class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        age = 2016 - self.year
        return age

    def is_vintage(self):
        if self.get_age() > 50:
            return True
        return False

    def __str__(self):
        return "{}, {} typing, Reflection = {}, First appeared in.".format(self.name, self.year, self.cost)
