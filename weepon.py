class weapon:
    def __init__(self,name,category,damage):
        self.name=name
        self.category=category
        self.damage=damage

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")

class Melee(weapon):
    def __init__(self, name, category, damage, damage_category):
        super().__init__(self, name, category, damage, damage_category)

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")
        print(f"Damage Category: {self.damage_category}")

class Range(weapon):
    def __init__(self, name, category, damage, damage_category, range):
        super().__init__(self, name, category, damage, damage_category, range)

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")
        print(f"Damage Category: {self.damage_category}")
        print(f"Range: {self.range}")

class BigRange(Range):
    def __init__(self, name, category, damage, damage_category, range):
        super().__init__(self, name, category, damage, damage_category, range)

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")
        print(f"Damage Category: {self.damage_category}")
        print(f"Range: {self.range}")

class SmallRange(Range):
    def __init__(self, name, category, damage, damage_category, range):
        super().__init__(self, name, category, damage, damage_category, range)

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")
        print(f"Damage Category: {self.damage_category}")
        print(f"Range: {self.range}")