class Plants:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self._height = round(height, 1)
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")


class Flower(Plants):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def show(self) -> None:
        super().show()
        print(f" color: {self.color}")

    def bloom(self) -> None:
        print(f""" {self._name} has not bloomed yet
[asking {self._name.casefold()} to bloom]""")
        self.show()
        print(f" {self._name} is blooming beautifully!")


class Tree(Plants):
    def __init__(self, name: str, height: float, age: int,
                 trunk_dia: float) -> None:
        super().__init__(name, height, age)
        self.diameter = trunk_dia

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.diameter, 1)}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]"
              f"Tree {self._name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self.diameter, 1)}cm wide.""")


class Vegetable(Plants):
    def __init__(self, name: str, height: float, age: int, season: str,
                 value: int) -> None:
        super().__init__(name, height, age)
        self.h_season = season
        self.n_value = value

    def show(self) -> None:
        super().show()
        print(f""" Harvest season: {self.h_season}
Nutrinional value: {self.n_value}""")

    def grow(self, growth: int) -> None:
        print(f"[make {self._name.casefold()} grow and age for {growth} days]")
        i = 1
        days = range(i, round(growth) + 1)
        for i in days:
            self._height += 2.1
            self._age += 1
            self.n_value += 1


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    print(" ")

    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print(" ")

    print("=== Vegetable")
    tomato = Vegetable("tomato", 5.0, 10, "April", 0)
    tomato.show()
    tomato.grow(20)
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
