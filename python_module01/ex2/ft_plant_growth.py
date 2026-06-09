class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.growth = float(0)
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm, {self.age} days old")

    def grow(self, height: float) -> None:
        self.height += height
        self.growth += height

    def age_plus(self, age: int) -> None:
        self.age += age


def ft_plant_grow() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("rose", 25, 30)
    rose.show()
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        rose.grow(0.8)
        rose.age_plus(1)
        rose.show()
    print(f"Growth this week: {rose.growth}cm")


if __name__ == "__main__":
    ft_plant_grow()
