# Assignment 1

class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.level = level

    def introduce(self):
        return f"I am {self.name}, I possess {self.power}, and I am level {self.level}!"

    def use_power(self):
        return f"{self.name} uses {self.power}!"


class Speedster(Superhero):
    def __init__(self, name, level, speed):
        super().__init__(name, "Super Speed", level)
        self.speed = speed

    def use_power(self):
        return f"{self.name} dashes at {self.speed} km/h!"


# Activity 2

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement move()")


class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"


# Demonstration
if __name__ == "__main__":
    hero = Superhero("Iron Blade", "Laser Vision", 7)
    fast_hero = Speedster("Flashburn", 9, 850)

    print(hero.introduce())
    print(hero.use_power())
    print(fast_hero.introduce())
    print(fast_hero.use_power())

    print("\n--- Polymorphism Demo ---")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        print(v.move())
