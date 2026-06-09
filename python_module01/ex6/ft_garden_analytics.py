class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._stats = self.Stats()

    @staticmethod
    def older_than_a_year(age: int) -> bool:
        if age > 365:
            return True
        else:
            return False

    @classmethod
    def anonymous(cls, name: str = 'Unknown plant',
                  height: float = 0.0, age: int = 0):  # type: ignore
        return cls(name, height, age)

    def bloom(self) -> None:
        self._stats.bloom_stats += 1

    def grow(self, grow_rate: float, duration: int) -> None:
        for day in range(duration):
            self._height += grow_rate
        self._stats.grow_stats += 1

    def age(self, duration: int) -> None:
        self._age += duration
        self._stats.age_stats += 1

    def show(self) -> None:
        print(f"{self._name.capitalize()}: "
              f"{round(self._height, 1)}cm, {self._age} days old")
        self._stats.show_stats += 1

    class Stats:
        def __init__(self) -> None:
            self.grow_stats = 0
            self.age_stats = 0
            self.show_stats = 0
            self.shade_stats = 0
            self.bloom_stats = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_stats} grow, "
                  f"{self.age_stats} age, "
                  f"{self.show_stats} show")
            if self.shade_stats:
                print(f" {self.shade_stats} shade")


def display_stats(plant: Plant):
    print(f"[statistics for {plant._name.capitalize()}]")
    plant._stats.display()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if not self._stats.bloom_stats:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk: float):
        super().__init__(name, height, age)
        self._trunk = trunk

    def show(self) -> None:
        super().show()
        print(f" Trunk diamater: {self._trunk}cm")

    def shade(self) -> None:
        self._stats.shade_stats += 1
        print(f"Tree {self._name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self._trunk, 1)}cm wide.")


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, color: str, seeds: int):
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

    def update(self, seeds_add: int) -> None:
        self._seeds += seeds_add


def ft_garden_analytics():
    rose = Flower('rose', 15.0, 10, 'red')
    oak = Tree('oak', 200.0, 365, 5.0)
    seed = Seed('sunflower', 80.0, 45, 'yellow', 0)
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_than_a_year(400)}\n")
    print("=== Flower")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.grow(8, 1)
    rose.show()
    display_stats(rose)
    print("\n=== Tree")
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.shade()
    display_stats(oak)
    print("\n=== Seed")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.grow(1.5, 20)
    seed.age(20)
    seed.bloom()
    seed.update(42)
    seed.show()
    display_stats(seed)
    print("\n=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    display_stats(anonymous)


if __name__ == "__main__":
    ft_garden_analytics()
